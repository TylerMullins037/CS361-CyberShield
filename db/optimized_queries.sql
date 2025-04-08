CREATE INDEX idx_tva_asset_id ON tva_mapping(asset_id);
CREATE INDEX idx_tva_threat_name ON tva_mapping(threat_name);
CREATE INDEX idx_tva_risk_score ON tva_mapping(risk_score);
CREATE INDEX idx_tva_date ON tva_mapping(date);
CREATE INDEX idx_tva_likelihood_impact ON tva_mapping(likelihood, impact);

CREATE INDEX idx_threat_ip ON threat_data(ip_address);
CREATE INDEX idx_threat_domain ON threat_data(domain_name);
CREATE INDEX idx_threat_type ON threat_data(threat_type);
CREATE INDEX idx_threat_score ON threat_data(threat_score);
CREATE INDEX idx_threat_ports ON threat_data(ports);

CREATE INDEX idx_mitigation_tva_id ON mitigation_strategies(tva_mapping_id);
