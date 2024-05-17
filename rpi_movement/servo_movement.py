from gpiozero import Servo
import time

delay = 2.3
speed = 0.025

def dispense_pill(servo_pin_number):
    servo = Servo(servo_pin_number)
    servo.value = speed
    time.sleep(delay)
    servo.value = None
    time.sleep(delay)