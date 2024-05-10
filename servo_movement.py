from time import *
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

for i in range(4, 7):
    kit.servo[i].angle = 0

def rotate(channel):
    kit.continuous_servo[channel].throttle = 1
    sleep(2)
    kit.continuous_servo[channel].throttle = 0

rotate(4)
rotate(6)