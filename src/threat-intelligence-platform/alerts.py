import smtplib
import requests
import os
import json
import traceback
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv("threat-backend/.env")

# Debug environment variables
print(f"Sender Email: {os.getenv('ALERT_SENDER_EMAIL')}")
print(f"Receiver Email: {os.getenv('ALERT_RECEIVER_EMAIL')}")
print(f"SMTP Server: {os.getenv('SMTP_SERVER')}")
print(f"SMTP Port: {os.getenv('SMTP_PORT', 587)}")
print(f"SMTP User: {os.getenv('SMTP_USER')}")
print(f"SMTP Password: {'*****' if os.getenv('SMTP_PASSWORD') else 'Not set'}")
print(f"Webhook URL: {os.getenv('WEBHOOK_URL')}")

ALERTS_FILE = "alerts_sent.json"  # Store sent alerts to avoid duplicates
API_URL = "http://127.0.0.1:5000/api/high_risk_threats"

# Ensure alerts file exists
if not os.path.exists(ALERTS_FILE):
    with open(ALERTS_FILE, "w") as f:
        json.dump([], f)

def send_email_alert(threat, risk_score, mitigation_strategies):
    sender_email = os.getenv("ALERT_SENDER_EMAIL")
    receiver_email = os.getenv("ALERT_RECEIVER_EMAIL")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    smtp_user = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")
    
    # Validate email configuration
    if not all([sender_email, receiver_email, smtp_server, smtp_user, smtp_password]):
        print("❌ Email configuration incomplete. Check your .env file.")
        print(f"Missing: {' '.join([k for k, v in {'ALERT_SENDER_EMAIL': sender_email, 'ALERT_RECEIVER_EMAIL': receiver_email, 'SMTP_SERVER': smtp_server, 'SMTP_USER': smtp_user, 'SMTP_PASSWORD': smtp_password}.items() if not v])}")
        return False

    msg = MIMEText(f"⚠️ High-Risk Threat Detected: {threat} with Risk Score {risk_score}. \n Here are some ways to mitigate this threat: \n {mitigation_strategies}")
    msg["Subject"] = "🚨 Critical Cybersecurity Alert 🚨"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            print(f"Connecting to SMTP server {smtp_server}:{smtp_port}...")
            server.set_debuglevel(1)  # Enable debug output
            server.starttls()
            print(f"Logging in as {smtp_user}...")
            server.login(smtp_user, smtp_password)
            print(f"Sending email from {sender_email} to {receiver_email}...")
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print(f"✅ Email alert sent for {threat}")
            return True
    except Exception as e:
        print(f"❌ Failed to send email alert: {e}")
        traceback.print_exc()  # Print full stack trace
        return False

def send_webhook_alert(threat, risk_score, mitigation_strategies):
    webhook_url = os.getenv("WEBHOOK_URL")
    if not webhook_url:
        print("❌ Webhook URL not configured.")
        return False
    
    data = {"threat": threat, "risk_score": risk_score, "message": "⚠️ High-Risk Threat Detected"}
    try:
        print(f"Sending webhook to {webhook_url}...")
        response = requests.post(webhook_url, json=data)
        if response.status_code == 200:
            print(f"✅ Webhook alert sent for {threat}")
            return True
        else:
            print(f"❌ Failed to send webhook alert: {response.status_code} {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error sending webhook alert: {e}")
        traceback.print_exc()
        return False

def get_previously_alerted():
    try:
        with open(ALERTS_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️ Error reading alerts file: {e}")
        traceback.print_exc()
        return []

def save_alerted_threats(alerted_threats):
    try:
        with open(ALERTS_FILE, "w") as f:
            json.dump(alerted_threats, f)
    except Exception as e:
        print(f"⚠️ Error saving alerts file: {e}")
        traceback.print_exc()

def fetch_and_alert():
    try:
        print(f"Fetching threats from {API_URL}...")
        response = requests.get(API_URL)
        if response.status_code != 200:
            print(f"❌ Failed to fetch high-risk threats from API: {response.status_code} {response.text}")
            return
        
        threats = response.json()
        print(f"Threats received: {threats}")
        
        if not threats:
            print("ℹ️ No high-risk threats found.")
            return
            
        alerted_threats = get_previously_alerted()
        print(f"Previously alerted threats: {alerted_threats}")
        
        for threat in threats:
            threat_name = threat["threat"]
            risk_score = threat["risk_score"]
            mitigation_strategy =threat["strategies"]
            
            # Only alert if this threat hasn't been sent before
            if threat_name not in alerted_threats:
                print(f"New threat detected: {threat_name} with score {risk_score}")
                email_sent = send_email_alert(threat_name, risk_score, mitigation_strategy)
                webhook_sent = send_webhook_alert(threat_name, risk_score,mitigation_strategy)
                
                if email_sent or webhook_sent:
                    alerted_threats.append(threat_name)
                    save_alerted_threats(alerted_threats)
            else:
                print(f"Threat already alerted: {threat_name}")
    except Exception as e:
        print(f"⚠️ Error in fetching and alerting: {e}")
        traceback.print_exc()

def test_email_connection():
    """Test the email connection without sending an actual alert"""
    sender_email = os.getenv("ALERT_SENDER_EMAIL")
    receiver_email = os.getenv("ALERT_RECEIVER_EMAIL")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    smtp_user = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")
    
    print("\n--- Testing Email Connection ---")
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            print(f"Connecting to SMTP server {smtp_server}:{smtp_port}...")
            server.set_debuglevel(1)  # Enable debug output
            server.starttls()
            print(f"Logging in as {smtp_user}...")
            server.login(smtp_user, smtp_password)
            print("✅ SMTP connection successful!")
            return True
    except Exception as e:
        print(f"❌ SMTP connection failed: {e}")
        traceback.print_exc()
        return False

# Run the alert system
if __name__ == "__main__":
    print("Starting cybersecurity alert system...")
    test_email_connection()  # First test if email connection works
    fetch_and_alert()
    print("Alert process completed.")
