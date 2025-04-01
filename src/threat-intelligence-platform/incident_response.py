import asyncio
import psycopg2
from ollama import chat
import re

def get_db_connection():
    return psycopg2.connect(
        dbname="defaultdb",
        user="doadmin",
        password="*************",
        host="db-postgresql-nyc3-21525-do-user-20065838-0.k.db.ondigitalocean.com",
        port="25060"
    )

def fetch_threat_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, asset_id, threat_name, vulnerability_description FROM tva_mapping;")
    threats = cursor.fetchall()
    conn.close()
    return threats

async def response_recommendation(threat_description):
    # LLM Refinement
    try:
        response = chat(model='deepseek-r1:1.5b', messages=[{
            'role': 'system',
            'content': f""" 
            You are an expert in cybersecurity analysis. Please evaluate the following threat description based on current industry trends and standards. 
            For the given threat, provide ONLY ONE ONLY ONE ONLY ONE ONLY ONE ONLY ONE ONLY ONE recommended response plan to reduce or eliminate the risk associated with it. 
            Your recommendations should focus on practical, actionable measures such as security controls, best practices, or industry standards. 
            Consider factors such as the latest security frameworks, attack vectors, and relevant technology. Link detected threats to NIST’s Incident Handling Guide (SP 800-61 Rev. 2)
            Please respond strictly in the following format: 'Response Plan: [one plan]'' where the plan is specific, clear, and focused on actionable solutions.
            Threat: {threat_description} 
            """
        }])
        # Get the raw response content
        response_content = response.get('message', {}).get('content', '')
        match = re.search(r"Response Plan:\s*(.*)", response_content, re.DOTALL)
        
        if match:
            # Clean and format the extracted response plan
            response_plan = match.group(1).strip()
            return response_plan
        else:
            return "No Available Response Recommendations"  # Fallback if not found
    except Exception as e:
        print(f"Error during response plan extraction: {e}")
        return "No Available Response Recommendations"  # Fallback values

async def update_recommendations():
    threats = fetch_threat_data()
    conn = get_db_connection()
    cursor = conn.cursor()
    
    for tva_id, asset_id, threat_name, vulnerability_description in threats:
        threat_description = threat_name + " " + vulnerability_description
        recommendation = await response_recommendation(threat_description)
        
        response_bullets = recommendation.split('1. ')[1:]  # Exclude the first empty element
        response_bullets = ['1. ' + bullet.strip() for bullet in response_bullets]  # Add the "1." back
        print(response_bullets)
        
        for bullet in response_bullets:
            cursor.execute(
                """
                INSERT INTO public.incident_logs (tva_mapping_id, response_plan)
                VALUES (%s, %s);
                """,
                (tva_id, recommendation)
            )
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    asyncio.run(update_recommendations())
