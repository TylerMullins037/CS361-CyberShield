CREATE TABLE alert_logs (
    id SERIAL PRIMARY KEY,
    tva_mapping_id INT REFERENCES tva_mapping(id),
    alert_date DATE DEFAULT CURRENT_DATE,
    alert_log TEXT
);
