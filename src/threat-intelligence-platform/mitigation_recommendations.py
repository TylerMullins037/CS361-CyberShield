def recommend_mitigation(threat):
    # Dictionary mapping threats to mitigation strategies
    recommendations = {
        "SQL Injection": "Enable parameterized queries and use a Web Application Firewall (WAF).",
        "Phishing": "Enforce two-factor authentication and train employees on phishing awareness.",
        "DDoS": "Implement rate limiting and use DDoS protection services.",
        "Ransomware": "Use endpoint protection, conduct regular backups, and implement network segmentation.",
        "Cross-Site Scripting (XSS)": "Sanitize user inputs and use Content Security Policy (CSP).",
        "Malware": "Deploy anti-malware software and enforce strict network access controls.",
        "Man-in-the-Middle (MITM)": "Use encryption (TLS/SSL) and ensure proper certificate validation.",
        "Insider Threat": "Monitor user activity, implement least-privilege access, and conduct regular audits.",
        "Broken Authentication": "Implement multi-factor authentication and secure password policies.",
        "Data Breach": "Encrypt sensitive data and limit access to authorized users only."
    }

    # Return the recommendation based on the detected threat, defaulting to a message if not found
    return recommendations.get(threat, "No recommendation available for this threat.")

# Example usage
detected_threat = "Phishing"
mitigation = recommend_mitigation(detected_threat)
print(f"Recommended Mitigation for {detected_threat}: {mitigation}")