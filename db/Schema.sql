CREATE TABLE assets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(50),
    description TEXT
);

CREATE TABLE threats (
    id SERIAL PRIMARY KEY,
    asset_id INT REFERENCES assets(id) ON DELETE CASCADE,
    threat_name VARCHAR(255) NOT NULL,
    risk_level INT CHECK (risk_level BETWEEN 1 AND 10),
    description TEXT
);

CREATE TABLE vulnerabilities (
    id SERIAL PRIMARY KEY,
    asset_id INT REFERENCES assets(id) ON DELETE CASCADE,
    vulnerability_name VARCHAR(255) NOT NULL,
    severity_level INT CHECK (severity_level BETWEEN 1 AND 10),
    description TEXT
);

CREATE TABLE risk_ratings (
    id SERIAL PRIMARY KEY,
    asset_id INT REFERENCES assets(id) ON DELETE CASCADE,
    threat_id INT REFERENCES threats(id) ON DELETE CASCADE,
    vulnerability_id INT REFERENCES vulnerabilities(id) ON DELETE CASCADE,
    impact INT CHECK (impact BETWEEN 1 AND 10),
    likelihood INT CHECK (likelihood BETWEEN 1 AND 10),
    risk_rating INT GENERATED ALWAYS AS (impact * likelihood) STORED
);
