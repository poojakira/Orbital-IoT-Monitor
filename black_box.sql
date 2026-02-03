CREATE TABLE mission_logs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    altitude FLOAT,
    heat_flux FLOAT,
    anomaly_score FLOAT,
    status VARCHAR(50)
);