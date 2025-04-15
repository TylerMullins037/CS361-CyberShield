EXPLAIN ANALYZE SELECT * FROM tva_mapping WHERE risk_score >20;


SELECT 
    t.threat_name,
    ms.mitigation_strategy
FROM 
    tva_mapping t
JOIN 
    mitigation_strategies ms ON t.id = ms.tva_mapping_id
