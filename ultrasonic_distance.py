import RPi.GPIO as GPIO
import time

# Pin assignments
TRIG = 14
ECHO = 15

# System initialization
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

try:
    while True:
        # Trigger the sensor pulse
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        # Track travel duration
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()
            
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()
            
        # Physics conversion equation to calculate distance
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        
        print(f"📊 Distance: {distance} cm")
        time.sleep(1)

except KeyboardInterrupt:
    print("\n🛑 Exiting distance tracking pipeline...")
finally:
    GPIO.cleanup()
