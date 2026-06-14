import RPi.GPIO as GPIO
import time

# Pin assignment
ir_pin = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(ir_pin, GPIO.IN)

try:
    while True:
        ir_value = GPIO.input(ir_pin)
        
        # Binary state check logic (0 = Object Close, 1 = Clear Line)
        if ir_value == 0:
            print("🚨 Alert: Object Detected!")
            time.sleep(1)
        else:
            print("🟢 Status: Object not detected")
            time.sleep(1)

except KeyboardInterrupt:
    print("\n🛑 Sensor stopped by user.")
finally:
    GPIO.cleanup()
