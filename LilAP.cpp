#include <WiFi.h>
#include <AsyncTCP.h>
#include <ESPAsyncWebServer.h>
#include <LittleFS.h>

// Network Credentials for Local AP Mode
const char* ap_ssid = "LocalDevKit_C3";
const char* ap_pass = "gamedev123"; // Min 8 chars for WPA2

// Create AsyncWebServer object on port 80
AsyncWebServer server(80);

void setup() {
  Serial.begin(115200);
  delay(1000);

  // Initialize LittleFS (or swap with SD.begin() if using an SD card module)
  if (!LittleFS.begin(true)) {
    Serial.println("An Error has occurred while mounting LittleFS");
    return;
  }
  Serial.println("Filesystem mounted successfully.");

  // Configure ESP32-C3 as an Access Point
  WiFi.softAP(ap_ssid, ap_pass);
  IPAddress IP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(IP);

  // Route for root / index.html
  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send(LittleFS, "/index.html", "text/html");
  });

  // Serve all static assets (scripts, wasm blobs, editors) from root directory
  server.serveStatic("/", LittleFS, "/").setDefaultFile("index.html");

  // Handle 404s
  server.onNotFound([](AsyncWebServerRequest *request){
    request->send(404, "text/plain", "Not found on ESP32-C3 Host.");
  });

  // Start server
  server.begin();
  Serial.println("Localhost web server active.");
}

void loop() {
  // Asynchronous server runs in background callbacks; loop remains lean.
  vTaskDelay(pdMS_TO_TICKS(1000));
}
