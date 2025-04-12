import subprocess #to run commands
import blue_team_defense
def automated_response(threat, ip=None):

    responses = {"SQL Injection": "Apply web application firewall (WAF) rules",
                 "Phishing": "Enforce 2 factor authentication and passkey",
                 "DDOS Attack": "Activate rate limiting and blockhole routing",
                 "Brute Force": "Implement accout lockout after 4 failed attempts",
                 "Malware": "Please isolate the infected system into a sandbox"}

    #applying measure
    action = responses.get(threat, "No Automatic responsible available")

    if threat == "DDOS Attack":
        blue_team_defense.block(ip, "DDOS  Attacked is detected")


    if threat == "Phishing":
        blue_team_defense.block(ip, "Phishing attacked is detected")

    return action

actions = automated_response("Phishing","8.8.8.8")
print("Recommended actions: {actions}".format(actions=actions))
