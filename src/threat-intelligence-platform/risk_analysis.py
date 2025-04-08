import asyncio
import psycopg2
from ollama import chat
from ollama import ChatResponse
import re
from risk_scoring import forecast_risk, time_weighted_score


def get_db_connection():
    return psycopg2.connect(
        dbname="defaultdb", user="doadmin", password="**********",
        host="db-postgresql-nyc3-21525-do-user-20065838-0.k.db.ondigitalocean.com", port="25060"
    )

def fetch_threat_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, asset_id, threat_name, vulnerability_description FROM tva_mapping;")
    threats = cursor.fetchall()
    conn.close()
    return threats

async def assign_likelihood_impact(threat_description):
    """
    Uses a rule-based approach + LLM-based refinement to calculate likelihood (L) and impact (I).
    """
    # Basic heuristic assignment
    likelihood, impact = {
        "ransomware": (3, 4),
        "phishing": (5, 4),
        "sql injection": (4, 5)
    }.get(threat_description.lower(), (2, 3))

    # LLM Refinement
    try:
        response = chat(model='deepseek-r1:1.5b', messages=[{
            'role': 'system',
            'content': f"""
            You are an expert in cybersecurity analysis. Please evaluate the following threat description based on current industry trends and standards.
            For each threat, assign a likelihood (1-5) and an impact (1-5) score. Use the following guidelines:
            - Likelihood: 1 = Very Unlikely, 5 = Very Likely
            - Impact: 1 = Minimal Impact, 5 = Severe Impact

            The analysis should only consider factors like historical industry data, common attack vectors, and technical vulnerabilities relevant to this specific threat. 

            Please respond strictly in the following format:
            'Likelihood: X, Impact: Y' 
            where X and Y are integers from 1 to 5. Do not include any additional text or explanation.

            Threat: {threat_description}
            """
        }])
        # Get the raw response content
        response_content = response.get('message', {}).get('content', '')

        # Look for any potential patterns of "Likelihood" and "Impact"
        likelihood_match = re.search(r'Likelihood\s*[:|-]?\s*(\d)', response_content, re.IGNORECASE)
        impact_match = re.search(r'Impact\s*[:|-]?\s*(\d)', response_content, re.IGNORECASE)
        # If both matches are found, return the extracted values
        if likelihood_match and impact_match:
            likelihood = int(likelihood_match.group(1))
            impact = int(impact_match.group(1))
            print(f"Extracted Likelihood: {likelihood}, Impact: {impact}")
            return likelihood, impact
        
    except Exception:
        pass
    return likelihood, impact  # Fallback values

from datetime import datetime

async def update_tva_mapping():
    threats = fetch_threat_data()
    conn = get_db_connection()
    cursor = conn.cursor()

    for tva_id, asset_id, threat_name, vulnerability_description in threats:
        likelihood, impact = await assign_likelihood_impact(threat_name + " " + vulnerability_description)
        
        # Get the threat's original detection date from tva_mapping
        cursor.execute("SELECT date FROM tva_mapping WHERE id = %s", (tva_id,))
        result = cursor.fetchone()
        threat_date = result[0] if result else datetime.today().date()

        # Step 1: Base risk
        base_score = likelihood * impact

        # Step 2: Time-weighted adjustment
        weighted_score = await time_weighted_score(base_score, threat_date)

        cursor.execute("""
            SELECT EXTRACT(DOY FROM detected_at)::int, risk_score 
            FROM risk_history 
            WHERE tva_id = %s
            ORDER BY detected_at ASC;
        """, (tva_id,))
        trend_data = cursor.fetchall()
        forecasted_risk = 0
        if trend_data:
            forecasted_risk = await forecast_risk(trend_data)
        # Optional: You can blend actual weighted score and forecast for proactive response
        final_score = round((weighted_score + forecasted_risk) / 2, 2)

        # Update the table with time-weighted + forecasted score
        cursor.execute("""
            UPDATE tva_mapping
            SET likelihood = %s, impact = %s, risk_score = %s
            WHERE id = %s;
        """, (likelihood, impact, final_score, tva_id))

        # Also log the new risk score into risk_history
        cursor.execute("""
            INSERT INTO risk_history (tva_id, risk_score, detected_at)
            VALUES (%s, %s, %s);
        """, (tva_id, final_score, datetime.today().date()))

    conn.commit()
    conn.close()
    print("Risk scores updated with trend + time-weighted logic!")


if __name__ == "__main__":
    asyncio.run(update_tva_mapping())
    
