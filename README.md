# Astraeus-9-C-C

ASTRAEUS-9 is a fault-tolerant mission control system overseeing activities during orbital re-entry. The system achieves real-time hardware degradation detection through embedded hardware sensing, physics-driven simulation, and machine learning.

---

## 1. Overview

The system integrates 3 core technologies:

1. **ESP32 Embedded Sensing Kernel** with Kalman filtering for real-time hardware telemetry
2. **Physics-Based Re-Entry Simulator** modeling orbital decay from 550 km LEO to impact
3. **Neural Anomaly Detection** using MLP Autoencoder with reconstruction error analysis

---
## Project Background

Astraeus-9 began as a hardware-centric experiment to explore how much operational insight a small satellite or testbed can gain from an ESP32-class sensing stack.  
I consolidated those efforts into a cohesive project that:

- Streams telemetry from an ESP32-based sensing kernel
- Applies Kalman filtering and physics-based models for orbital and re-entry state estimation
- Drives a containerized Streamlit dashboard with real-time visualizations and anomaly flags

It serves as a bridge between embedded constraints and ML-driven orbital monitoring workflows.

---
## 2. System Architecture

| Module | Language | Role |
|---|---|---|
| `Astraeus_Kernel.ino` | C++ (Arduino) | ESP32 embedded sensing kernel + Kalman filter |
| `Kalman_Filter.h` | C++ | SpatialKalman filter header library |
| `mission_simulator.py` | Python | Orbital decay simulation from 550 km LEO to impact |
| `physics_engine.py` | Python | Atmospheric density + orbital torque computation |
| `thermodynamics.py` | Python | Re-entry heat flux and skin temperature modeling |
| `anomaly_ml.py` | Python | MLP Regressor Autoencoder for hardware fault detection |
| `main.py` | Python | Streamlit mission control dashboard entry point |
| `black_box.sql` | SQL | Postgres schema for mission-critical telemetry logs |

---

## 3. Quick Start

### Prerequisites

- Docker & Docker Compose
- Python 3.9+ (for local simulation)

### Initialization

```bash
# Step 1: Initialize services (Mosquitto Broker + Postgres DB + Streamlit Dashboard)
bash setup.sh

# Step 2: Launch orbital decay simulation
python mission_simulator.py

# Step 3: Access Dashboard
# Navigate to: http://localhost:8501
```

---

## 4. Physics Simulation

| Parameter | Value |
|---|---|
| Starting Altitude (LEO) | 550 km |
| Decay Model | Atmospheric drag |
| Anomaly Injection | Cosmic Ray Bit-Flips + radiation damage |
| Thermal Model | Re-entry heat flux + skin temperature estimation |
| Orbital Torque | Computed by `physics_engine.py` |

---

## 5. ML Anomaly Detection

| Parameter | Value |
|---|---|
| Model Type | MLP Regressor Autoencoder |
| Detection Method | Reconstruction error analysis |
| Hardware Fault Categories | Cosmic Ray Bit-Flips, radiation damage, sensor degradation |
| Dashboard Analysis | Neural spectral analysis for hardware condition assessment |

---

## 6. Infrastructure

- **Docker Compose**: Containerizes Mosquitto MQTT broker, Postgres database, and Streamlit dashboard
- **MQTT Protocol**: ESP32 transmits telemetry over WiFi via MQTT to `astraeus/telemetry` topic
- **Postgres**: Persists flight data (timestamp, altitude, heat flux, anomaly scores) in `mission_logs` table
- **Streamlit UI**: Custom dark mode (`style.css`) with real-time kinetic vector visualization

---

## 7. Dependencies

- **Python**: `streamlit`, `numpy`, `scikit-learn`, `paho-mqtt`, `plotly`, `scipy`, `psycopg2-binary`
- **Services**: `eclipse-mosquitto`, `postgres:latest`

---

## 8. Team Contributions

### Pooja Kiran — Lead ML & Data Engineering Engineer

| # | Contribution Area | Details | Quantified Impact |
|---|---|---|---|
| 1 | Neural Anomaly Detection Engine | Designed and implemented `anomaly_ml.py`: MLP Regressor Autoencoder evaluating hardware faults through reconstruction error analysis | Detects Cosmic Ray Bit-Flips, radiation damage, and sensor degradation in real time |
| 2 | Postgres Telemetry Schema | Designed `black_box.sql`: Postgres schema persisting mission-critical telemetry and diagnostic logs | Stores timestamp, altitude, heat flux, and anomaly scores for full mission-critical audit trail |
| 3 | Streamlit Mission Control Dashboard | Built `main.py`: Streamlit-based UI with custom dark mode (`style.css`), real-time kinetic vector visualization, and neural spectral analysis for hardware condition assessment | Full-stack dashboard at localhost:8501; custom CSS dark mode for operational clarity |
| 4 | Docker Infrastructure | Containerized the full platform via Docker Compose: Mosquitto MQTT broker + Postgres DB + Streamlit dashboard; scripted initialization via `setup.sh` | 3-service Docker Compose deployment; one-command `bash setup.sh` initialization |

### Rhutvik Pachghare — Lead Robotics, GNC & Embedded Systems Engineer

| # | Contribution Area | Details | Quantified Impact |
|---|---|---|---|
| 1 | ESP32 Embedded Sensing Kernel | Implemented `Astraeus_Kernel.ino`: ESP32 microcontroller firmware running SpatialKalman filter (`Kalman_Filter.h`) for real-time sensor data smoothing and velocity estimation | SpatialKalman filter processes raw sensor data to produce smoothed telemetry + velocity estimations |
| 2 | SpatialKalman Filter Library | Designed `Kalman_Filter.h`: C++ header library implementing the SpatialKalman filtering algorithm for 3-axis orbital state estimation | Embedded Kalman filter running on ESP32 hardware; reduces raw sensor noise in real time |
| 3 | MQTT Telemetry Communications | Configured ESP32 telemetry transmission via MQTT protocol over WiFi to `astraeus/telemetry` topic | Real-time wireless telemetry pipeline from ESP32 hardware to cloud MQTT broker |
| 4 | Physics-Based Re-Entry Simulator | Built `mission_simulator.py`: models orbital decay from 550 km LEO to impact; uses atmospheric drag to simulate increasing jitter with altitude; injects Cosmic Ray Bit-Flips and radiation damage anomalies | Simulates full LEO-to-impact re-entry trajectory; publishes telemetry to MQTT topic |
| 5 | Thermodynamic & Physics Engines | Implemented `physics_engine.py` (atmospheric density + orbital torque) and `thermodynamics.py` (re-entry heat flux + skin temperature) | Quantifies thermal and mechanical loading during re-entry at each altitude step |
| 6 | Repository Documentation & CODEOWNERS | Restructured README for engineering domain separation and established `CODEOWNERS.md` defining technical ownership | Clear GNC vs ML domain separation; CODEOWNERS.md governs code review assignments |

---

**License**: Private | **Platform**: ESP32 + Python 3.9+ | **Protocol**: MQTT over WiFi
