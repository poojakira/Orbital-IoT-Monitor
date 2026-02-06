# Astraeus-9-C-C

The ASTRAEUS-9 system functions as a fault-tolerant mission control system which oversees activities during orbital re-entry. The system uses three technologies to achieve real-time hardware degradation detection through embedded hardware sensing and physics-driven simulation and machine learning.

**System Architecture**
1. Embedded Kernel (/Astraeus_Kernel.ino)

Platform: ESP32 Microcontroller 


Logic: The system operates SpatialKalman filter (Kalman_Filter.h) which processes raw sensor data to produce smoothed results and velocity estimations.

Comms: The system sends telemetry data by using MQTT protocol to transmit over WiFi to the broker.

**2. Mission Simulation (/mission_simulator.py)**

Scenario: The system models an orbital decay process which starts from 550km (LEO) and ends with an impact.

Physics: The system uses atmospheric drag to create a model which shows increasing "jitter" effects that happen when altitude decreases.

Anomaly Injection: The system uses random methods to introduce "Cosmic Ray Bit-Flips" and radiation damage according to the duration of exposure.

**3. Intelligence & Physics Engines**

anomaly_ml.py: The MLP Regressor (Autoencoder) system evaluates hardware faults through reconstruction error analysis.

physics_engine.py: The system computes both atmospheric density and orbital torque.

thermodynamics.py: The system creates a model for re-entry heat flux and skin temperature estimates.

4. Mission Control Dashboard (/main.py)

Interface: The interface uses Streamlit to create a UI which displays a "dark mode" CSS theme.

Modules:


Telemetry: The system provides real-time displays of kinetic vector data.

Diagnostics: The system uses neural spectral analysis to assess hardware condition.

Thermal Re-entry: The system creates detailed aerodynamic thermal profiles of re-entry vehicles.

**Infrastructure & Setup**

The system uses Docker to create containerized environments which manage the MQTT broker and Postgres database and Python dashboard.

**Prerequisites**

i. Docker & Docker Compose: The system requires Python version 3.9 or higher for local simulation purposes.

ii. Initialize Services: Execute the setup script to build and launch the container cluster:

                                                                                        bash setup.sh

This starts the Mosquitto Broker, Postgres DB, and Streamlit Dashboard.

iiii. Launch Simulation: In a separate terminal, start the telemetry generator:

                                                                          python mission_simulator.py

This will begin publishing data to astraeus/telemetry.

iv. Access Mission Control: Navigate to http://localhost:8501 to view live mission data.

**Dependencies**
Python: streamlit, numpy, scikit-learn, paho-mqtt, plotly, scipy, psycopg2-binary.

Services: eclipse-mosquitto, postgres:latest.

 **Data Logs**

Flight data is persisted to the mission_logs Postgres table, recording timestamp, altitude, heat flux, and anomaly scores


![Dashboard](https://github.com/user-attachments/assets/31d4fced-840b-4a10-8817-b493f7fad03e)


