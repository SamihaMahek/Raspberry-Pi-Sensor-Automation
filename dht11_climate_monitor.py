import Adafruit_DHT
import time

# Set sensor type and pin mapping
sensor = Adafruit_DHT.DHT11
pin = 14

print("🌡️ Starting Climate Monitor Logging Session...")

while True:
    # Read telemetry signals from DHT11 hardware
    hum, temp = Adafruit_DHT.read_retry(sensor, pin)
    
    if hum is not None and temp is not None:
        print(f"☀️ Temperature: {temp}°C")
        print(f"💧 Humidity: {hum}%")
        print("-" * 25)
    else:
        print("❌ Error: Failed to read data from DHT11 sensor matrix.")
        
    time.sleep(2)
