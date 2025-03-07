CREATE TABLE tva_mapping (
    id SERIAL PRIMARY KEY,
    asset_id INT REFERENCES assets(id),
    threat_name VARCHAR(255),
    vulnerability_description TEXT,
    likelihood INT CHECK (likelihood BETWEEN 1 AND 5),
    impact INT CHECK (impact BETWEEN 1 AND 5),
    risk_score INT GENERATED ALWAYS AS (likelihood * impact) STORED
);
