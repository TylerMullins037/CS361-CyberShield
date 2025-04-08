import logging
import os
if not os.path.exists("logs"):
    os.makedirs("logs")
logging.basicConfig(filename='logs/threat_events.log',
level=logging.INFO, format="%(asctime)s - %(levelname)s -%(message)s")
def log_threat(threat, risk_score):
    """Logs detected even with the risk score"""
    logging.info(f"{threat} detected with risk score: {risk_score}")

if __name__ =="__main__":

    log_threat("DDOS attack", 30)
