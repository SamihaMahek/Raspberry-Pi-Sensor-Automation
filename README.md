A collection of Python scripts developed during microcontroller lab courses to interface a Raspberry Pi board with physical hardware sensors.

---

## 🚀 Project Overview
This repository contains embedded automation scripts. Each script controls a Raspberry Pi microcontroller to read raw electronic signals from hardware inputs, process the telemetry values, and output structural metrics to a console terminal screen.

### Included Sensors & Features
* **🔊 Ultrasonic Distance Tracking (`ultrasonic_distance.py`):** Uses an HC-SR04 sensor to send sound wave triggers. The code monitors signal travel times and uses standard physics logic to convert duration measurements into precise real-time distances in centimeters.
* **🚨 Infrared Obstacle Detection (`ir_obstacle_detector.py`):** Interacts with an IR sensor module using a binary checking loop ($0$ = Obstacle Intercept, $1$ = Clear Path) to log real-time security line flags.
* **🌡️ DHT11 Climate Monitoring (`dht11_climate_monitor.py`):** Interfaces with a digital environmental module using time-delay error handling to capture structural temperature and relative humidity percentage data cycles.

---

## 🛠️ Technology Stack
* **Programming Language:** Python 3
* **Hardware Interface Library:** `RPi.GPIO` (Raspberry Pi Native GPIO Pins Controller)
* **Sensor Handling Framework:** `Adafruit_DHT`


.
