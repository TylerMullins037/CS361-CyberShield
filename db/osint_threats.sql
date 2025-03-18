CREATE TABLE osint_threats (
    id SERIAL PRIMARY KEY,
    asset_id INT REFERENCES assets(id) ON DELETE CASCADE,
    threat_name VARCHAR(255) NOT NULL,
    osint_source VARCHAR(100) NOT NULL, 
    ip_address INET,
    domain VARCHAR(255),
    ports INT[],
    services TEXT,
    risk_level INT CHECK (risk_level BETWEEN 1 AND 10),
    detected_at TIMESTAMP DEFAULT NOW()
);
