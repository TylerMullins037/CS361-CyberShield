import os
import subprocess #to run commands
from datetime import datetime
import logging #track events
import fetch_osint
def block(ip, reason="UNKnown"):
    """block function to check if the ip is safe  or unsafe based on threat intelligence data
    with automatic logging and database insertion for tracking"""
    if  ip in fetch_osint.WHITE_LISTED_IPS: #check if the ip is white listed
        print(f"{ip} is whitelisted")
        return
    try:
        #block ip with tables
        subprocess.run(["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"], check=True)
        print("[BLOCKED] {ip} due to: {reason}".format(ip=ip, reason=reason))
        with open ("auto-block_log.txt", "a") as f:
            #write to file
            f.write("{datatime.now()} - Blocked {ip} | Reason: {reason}".format(datetime.now(), reason=reason))

            #store in the database
            fetch_osint.store_threat_intelligence("Auto-Blocked IP".format(ip=ip))

               #catch error                                   reason,4 , 5, 4*5)
    except subprocess.CalledProcessError as e:
        print(f"[Error] failed to block {ip}: {e}")
