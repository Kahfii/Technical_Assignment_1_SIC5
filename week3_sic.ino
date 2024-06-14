#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#define MQ_PIN 34

const char* ssid = "Nama_WIFI";
const char* password = "Password_WIFI";
const char* serverName = "http://ip_address_server:5000/send"; 


void setup() {
  Serial.begin(115200); 
  pinMode(MQ_PIN, INPUT);
  
  WiFi.begin(ssid, password);
  Serial.print("Menghubungkan ke WIFI ..");
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print('.');
  }
  Serial.println("Terhubung ke WIFI");

}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverName);
    int sensorValue = analogRead(MQ_PIN);  
    Serial.print("NilaiSensor: ");
    Serial.println(sensorValue); 
  
    http.addHeader("Content-type", "application/json");

    StaticJsonDocument<200> doc;
    doc["NamaSender"] = "ESP32 microcontroller";
    doc["NilaiSensor"] = sensorValue;

    String requestBody;
    serializeJson(doc, requestBody);

    int httpResponseCode = http.POST(requestBody);

    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.println(httpResponseCode);
      Serial.println(response);
    } else {
      Serial.println("Terjadi Kesalahan saat mengirim POST:");
      Serial.println(httpResponseCode);
    }
      http.end();
  }
  delay(8000);
}
