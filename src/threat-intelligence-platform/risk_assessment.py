import openai
import psycopg2
from transformers import pipeline

# OpenAI API Key (replace with your actual key)
openai.api_key = ""  

# Database connection
def get_db_connection():
    return psycopg2.connect(
        dbname="shopsmart", user="admin", password="securepass", host="localhost"
    )

# Function to get asset and threat data
def fetch_threat_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT asset_id, threat_name, vulnerability_description FROM tva_mapping;")
    threats = cursor.fetchall()
    conn.close()
    return threats

# Assign likelihood and impact scores dynamically
def assign_likelihood_impact(threat_description):
    """
    Uses a rule-based approach + LLM-based refinement to calculate likelihood (L) and impact (I).
    """
    # Step 1: Basic heuristic assignment
    if "ransomware" in threat_description.lower():
        likelihood = 3
        impact = 4
    elif "phishing" in threat_description.lower():
        likelihood = 5
        impact = 4
    elif "sql injection" in threat_description.lower():
        likelihood = 4
        impact = 5
    else:
        likelihood = 2
        impact = 3  # Default values

    # Step 2: LLM Refinement (GPT-4)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a cybersecurity risk assessment assistant."},
            {"role": "user", "content": f"Analyze the following threat: {threat_description}. Assign a likelihood (1-5) and impact (1-5) based on industry trends."}
        ]
    )
    refined_data = response["choices"][0]["message"]["content"].split()

    try:
        refined_likelihood = int(refined_data[1]) if refined_data[1].isdigit() else likelihood
        refined_impact = int(refined_data[3]) if refined_data[3].isdigit() else impact
    except:
        refined_likelihood, refined_impact = likelihood, impact  # Fallback to heuristic scores

    return refined_likelihood, refined_impact

# Calculate risk score
def calculate_risk_scores():
    threats = fetch_threat_data()
    risk_results = []

    for asset_id, threat_name, vulnerability_description in threats:
        likelihood, impact = assign_likelihood_impact(threat_name + " " + vulnerability_description)
        risk_score = likelihood * impact  # Risk Score = L * I
        risk_results.append((asset_id, threat_name, likelihood, impact, risk_score))

    return risk_results

# Save risk scores to database
def save_risk_scores():
    conn = get_db_connection()
    cursor = conn.cursor()
    risk_data = calculate_risk_scores()

    for asset_id, threat_name, likelihood, impact, risk_score in risk_data:
        cursor.execute(
            "INSERT INTO risk_scores (asset_id, threat_name, likelihood, impact, risk_score) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (asset_id, threat_name) DO UPDATE SET likelihood = EXCLUDED.likelihood, impact = EXCLUDED.impact, risk_score = EXCLUDED.risk_score;",
            (asset_id, threat_name, likelihood, impact, risk_score)
        )

    conn.commit()
    conn.close()
    print("Risk scores updated successfully!")

# Run the risk assessment logic
if __name__ == "__main__":
    save_risk_scores()
