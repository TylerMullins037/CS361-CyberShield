import asyncio
import psycopg2
from ollama import chat
from ollama import ChatResponse
import re

def get_db_connection():
    return psycopg2.connect(
        dbname="defaultdb", user="doadmin", password="**********",
        host="**************", port="25060"
    )

def fetch_threat_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, asset_id, threat_name, vulnerability_description FROM tva_mapping;")
    threats = cursor.fetchall()
    conn.close()
    return threats

async def mitigation_recommendation(threat_description):

    # LLM Refinement
    try:
        response = chat(model='deepseek-r1:1.5b', messages=[{
            'role': 'system',
            'content': f"""
            You are an expert in cybersecurity analysis. Please evaluate the following threat description based on current industry trends and standards.

            For the given threat, provide ONLY ONE recommended mitigation strategies to reduce or eliminate the risk associated with it. Your recommendations should focus on practical, actionable measures such as security controls, best practices, or industry standards. Consider factors such as the latest security frameworks, attack vectors, and relevant technology.

            Please respond strictly in the following format:
            'Mitigation Strategies:  [one strategy]''
            where the strategies are specific, clear, and focused on actionable solutions.

            Threat: {threat_description}
            """
        }])
        # Get the raw response content
        response_content = response.get('message', {}).get('content', '')
        match = re.search(r"Mitigation Strategies:\s*(.*)", response_content, re.DOTALL)
    
        if match:
            # Clean and format the extracted mitigation strategies
            mitigation_strategies = match.group(1).strip()
            return mitigation_strategies
        else:
            return "No Available Mitigation Recommendations"  # Fallback if not found
    except Exception as e:
        print(f"Error during mitigation extraction: {e}")
        return "No Available Mitigation Recommendations"  # Fallback values

async def update_recommendations():
    threats = fetch_threat_data()
    conn = get_db_connection()
    cursor = conn.cursor()

    for tva_id, asset_id, threat_name, vulnerability_description in threats:
        threat_description = threat_name + " " + vulnerability_description
        recommendation = await mitigation_recommendation(threat_description)
        
        mitigation_bullets = recommendation.split('1. ')[1:]  # Exclude the first empty element
        mitigation_bullets = ['1. ' + bullet.strip() for bullet in mitigation_bullets]  # Add the "1." back
        print(mitigation_bullets)
        for bullet in mitigation_bullets:
            cursor.execute(
                    """
                    INSERT INTO public.mitigation_strategies (tva_mapping_id, mitigation_strategy)
                    VALUES (%s, %s);
                    """,
                    (tva_id, recommendation) 
            )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    asyncio.run(update_recommendations())
