class RiskPrioritizationModel:
    """A model prioritizing security threats based on weighted factors"""
    def __init__(self, weight=None):
        """Risk prioritized based on the weights """
        if weight is None:
            self.weight = {'base_risk': 0.4,
                           "impact": 0.25,
                           "likelihood": 0.15,
                           "time_sensitivity" : 0.2,
                           "asset_value": 0.10}
        #check if the weights summ to 1
        total = sum(self.weight.values())
        if (not (0.99 <= total <= 1.11)):
            raise ValueError ( f"Weights must sum to 1.0, got {total}")
    def calculate_score(self, threat):
        """calculated a composit score based on weighted factors"""
        score =(
                self.weight["base_risk"] * threat["base_risk"] +
                self.weight["impact"] * threat['impact']+
                self.weight["likelihood"] * threat["likelihood"] +
                self.weight["time_sensitivity"] * threat["time_sensitivity"] +
                self.weight["asset_value"] * threat["asset_value"]

        )
        return round(score, 2) #returns the total score
    def prioritize_threats(self, threats):
        #prioritizing threats based on calculated score
        for threat in threats:
            threat['score'] = self.calculate_score(threat)
            return sorted(threats, key=lambda x: x['score'], reverse=True)
    def get_critical_threats(self, threats, threshold=70):
        "Getting threats above 70 "
        prioritize = self.prioritize_threats(threats)
        return [threat for threat in prioritize if threat['score']>=threshold]
    def threat_based_real_time_factors(self, threats, active_incidents=None):
        """Adjust threat based on real time factors like active incidents"""
        active_incidents = active_incidents or []# if active incident is not passed, initialize it with empty list
        adjust_threats = [] #empty list to store

        #iterate over each threat
        for threat in threats:
            #create a shallow threat copy of current threat to avoid modification
            adjust_threat = threat.copy()
            #is the threat type in the active incidents
            if threat.get("type") in active_incidents:
                #if it is part of active_incidents, increase the time sensitivity and never exceeds 10
                adjust_threat["time_sensitivity"] = min(10, (threat.get("time_sensitivity", 5) * 1.5))

            #threat score is recalcuated /
            adjust_threat["score"] = self.calculate_score(adjust_threat)
            #append it to the threats type
            adjust_threats.append(adjust_threat)

            #sort the scores of each threat so that the threat with highest score appear first
        return sorted(adjust_threats, key=lambda x: x["composite_score"], reverse=True)
    def time_factors(self, threats, active=None):
        """This methods is to adjust threat prioritization dynamically based on real time data"""
        active = active or [] #if active is not passed, initialize it with empty list
        #adjust threat based on real time incidents
        adjust_threats = self.threat_based_real_time_factors(threats, active)
        return adjust_threats
def determine_base_risk(ports, service):
    #detemining the number of ports based on open ports and service
    if len(ports) > 5:
        base= 0.7 # risk is high if more than 5 ports are open
    elif len(ports) > 0:
        base= 0.5 # medium risk for open ports
    else:
        base = 0.1 #lowest risk
    impact = 0.7 if len(service) > 5 else 0.3
    return base, impact
def determine_likelihood(ports):
    "Determining the likelihood based on open ports"
    return 0.7 if len(ports) >3 else 0.2
