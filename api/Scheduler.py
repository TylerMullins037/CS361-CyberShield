import os
import time
import logging
import schedule
from fetch_osint import fetch_osint_updates

#configuring logging display levels of warning, critical, Error with time stamps
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", force=True)

#schedule to run every 6 hours
schedule.every(6).hours.do(fetch_osint_updates)
if __name__=="__main__":
    logging.info("OSINT Threat intelligence monitoring started...")
    while True:
        try:
            #check for schedule tasks
            logging.info("Checking Scheduled tasks...")
            schedule.run_pending()
            time.sleep(60) # check every 60 seconds
        except Exception as e:
            logging.error(f"Error in scheduler loop: {e}")

