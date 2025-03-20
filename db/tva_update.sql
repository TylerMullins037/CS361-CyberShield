UPDATE tva_mapping
SET likelihood = 5
WHERE threat_name = 'Phishing'
AND EXISTS (SELECT 1 FROM threat_data WHERE threat_data.threat_type =
'Phishing' AND threat_data.risk_score > 20);
