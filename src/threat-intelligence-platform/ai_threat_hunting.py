import asyncio
from ollama import chat
import re

async def predict_threat_behavior(log_row):
    threat_description = log_row.to_dict()
    # LLM Refinement
    try:
        response = chat(model='deepseek-r1:1.5b', messages=[{
            'role': 'system',
            'content': f""" 
             You are a cybersecurity analyst. Given the following suspicious security threat, analyze its nature, identify any indicators of compromise (IOCs), and predict the most likely next attack vectors. Consider techniques from the MITRE ATT&CK framework and real-world APT behaviors.
Provide a concise analysis and list 1 potential next steps the attacker might take, including their objectives and recommended mitigation actions.
Please respond strictly in the following format: 'Prediction: [one plan]'' where the next action is specific, clear, and focused.

{threat_description} 
            """
        }])
        # Get the raw response content
        response_content = response.get('message', {}).get('content', '')
        match = re.search(r"Prediction:\s*(.*)", response_content, re.DOTALL)
        
        if match:
            # Clean and format the extracted response plan
            response_plan = match.group(1).strip()
            return response_plan
        else:
            return "No Available predictions"  # Fallback if not found
    except Exception as e:
        print(f"Error during predictions extraction: {e}")
        return "No Available predictions"  # Fallback values


if __name__ == "__main__":
    asyncio.run(predict_threat_behavior("SQL Injection detected on login page"))
