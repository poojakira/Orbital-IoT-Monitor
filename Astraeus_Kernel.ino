#include <WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>
#include <ESP32Servo.h>
#include "Kalman_Filter.h"

SpatialKalman kf;
Servo gimbal;
WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(115200);
  gimbal.attach(13);
  pinMode(12, OUTPUT); // Buzzer
  xTaskCreatePinnedToCore(TaskSensing, "Sensing", 4000, NULL, 2, NULL, 1);
}

void TaskSensing(void *pv) {
  float dt = 0.1; 
  for(;;) {
    float raw = analogRead(34); 
    float filtered = kf.filter(raw, dt);
    
    StaticJsonDocument<256> doc;
    doc["dist"] = filtered;
    doc["v"] = kf.getVelocity();
    
    char buffer[256];
    serializeJson(doc, buffer);
    client.publish("astraeus/telemetry", buffer);
    vTaskDelay(pdMS_TO_TICKS(100));
  }
}
void loop() {}