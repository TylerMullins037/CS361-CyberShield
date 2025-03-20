import smtplib
import requests
import os
import json
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv("src/.env")

ALERTS_FILE = "alerts_sent.json"  # Store sent alerts to avoid duplicates
API_URL = "http://127.0.0.1:5000/api/high_risk_threats"

# Ensure alerts file exists
if not os.path.exists(ALERTS_FILE):
    with open(ALERTS_FILE, "w") as f:
        json.dump([], f)

def send_email_alert(threat, risk_score):
    sender_email = os.getenv("ALERT_SENDER_EMAIL")
    receiver_email = os.getenv("ALERT_RECEIVER_EMAIL")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    smtp_user = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")

    msg = MIMEText(f"⚠️ High-Risk Threat Detected: {threat} with Risk Score {risk_score}")
    msg["Subject"] = "🚨 Critical Cybersecurity Alert 🚨"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print(f"✅ Email alert sent for {threat}")
    except Exception as e:
        print(f"❌ Failed to send email alert: {e}")

def send_webhook_alert(threat, risk_score):
    webhook_url = os.getenv("WEBHOOK_URL")
    if not webhook_url:
        print("❌ Webhook URL not configured.")
        return

    data = {"threat": threat, "risk_score": risk_score, "message": "⚠️ High-Risk Threat Detected"}
    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code == 200:
            print(f"✅ Webhook alert sent for {threat}")
        else:
            print(f"❌ Failed to send webhook alert: {response.status_code} {response.text}")
    except Exception as e:
        print(f"❌ Error sending webhook alert: {e}")

def get_previously_alerted():
    try:
        with open(ALERTS_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️ Error reading alerts file: {e}")
        return []

def save_alerted_threats(alerted_threats):
    try:
        with open(ALERTS_FILE, "w") as f:
            json.dump(alerted_threats, f)
    except Exception as e:
        print(f"⚠️ Error saving alerts file: {e}")

def fetch_and_alert():
    try:
        response = requests.get(API_URL)
        if response.status_code != 200:
            print("❌ Failed to fetch high-risk threats from API")
            return

        threats = response.json()
        alerted_threats = get_previously_alerted()

        for threat in threats:
            threat_name = threat["name"]
            risk_score = threat["risk_score"]

            # Only alert if this threat hasn't been sent before
            if threat_name not in alerted_threats:
                send_email_alert(threat_name, risk_score)
                send_webhook_alert(threat_name, risk_score)
                alerted_threats.append(threat_name)

        save_alerted_threats(alerted_threats)

    except Exception as e:
        print(f"⚠️ Error in fetching and alerting: {e}")

# Run the alert system
if __name__ == "__main__":
    fetch_and_alert()
