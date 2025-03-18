CREATE TABLE threat_data (
    id SERIAL PRIMARY KEY,           
    ip_address VARCHAR(45) NOT NULL, 
    ports INT[],                     
    services TEXT[]                  
);
