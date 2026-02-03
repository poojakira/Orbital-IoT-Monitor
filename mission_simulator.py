import paho.mqtt.client as mqtt
import json
import time
import numpy as np
import random

# Configuration
BROKER = "localhost"
TOPIC = "astraeus/telemetry"
client = mqtt.Client("MISSION_SIMULATOR")

def generate_telemetry(alt, health_factor=1.0):
    """
    Generates realistic sensor data influenced by altitude and radiation.
    health_factor: 1.0 = Healthy, < 0.5 = Radiation Damage
    """
    # Base physics: as altitude drops, jitter increases
    jitter = (1.0 / (alt/1000)) * 5 
    
    # Simulate Cosmic Ray Bit-Flip (Anomaly)
    if random.random() > (0.95 * health_factor):
        dist = random.uniform(500, 1000) # Impossible spike
    else:
        dist = 45.0 + np.random.normal(0, jitter)

    return {
        "sensor_id": "SAT_01",
        "dist": round(dist, 2),
        "temp": round(25.0 + (500000/alt)**2, 2), # Temp rises as alt drops
        "volt": round(3.9 + np.random.normal(0, 0.05), 2),
        "alt": round(alt, 2)
    }

def run_mission():
    print("🚀 Starting Simulated Re-entry Mission...")
    client.connect(BROKER, 1883)
    
    altitude = 550000.0  # Start at 550km (LEO)
    velocity = 7500.0    # 7.5 km/s
    health = 1.0         # 100% hardware health

    try:
        while altitude > 0:
            # 1. Simulate Orbital Decay (Physics)
            # Drag increases as altitude decreases
            drag = 0.0001 * (500000 / altitude)**2
            altitude -= (1000 + drag) 
            
            # 2. Simulate Radiation accumulation
            if altitude < 100000:
                health -= 0.01 # Hardware degrading from heat/plasma
            
            # 3. Generate and Publish
            payload = generate_telemetry(altitude, health)
            client.publish(TOPIC, json.dumps(payload))
            
            # 4. Console Log for Debugging
            status = "NOMINAL" if health > 0.8 else "DEGRADED"
            print(f"Alt: {altitude/1000:.2f}km | Health: {status} | Data: {payload['dist']}mm")
            
            time.sleep(0.5) # Fast-forward simulation
            
    except KeyboardInterrupt:
        print("\nMission Aborted by Ground Control.")
    finally:
        client.disconnect()

if __name__ == "__main__":
    run_mission()