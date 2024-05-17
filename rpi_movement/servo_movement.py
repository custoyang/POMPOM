from gpiozero import Servo
import time

delay = 3.3
speed = 0.025
servo1 = Servo(12)
servo2 = Servo(13)
servo3 = Servo(18)
servo4 = Servo(19)


def dispense_pill(servo):
    servo.value = speed
    time.sleep(delay)
    servo.value = None
    time.sleep(delay)