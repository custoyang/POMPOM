from gpiozero import Servo
import time
import servo_movement

class Compartment:
    def __init__(self, pin, pillCount, pill, frequency, size):
        self.pin = Servo(pin)
        self.pillCount = pillCount
        self.pill = pill
        self.frequency = frequency # in hours
        self.size = size
        self.delay = 3.3
        self.speed = 0.025
    
    def calibration(self, new_size):
        servo = Servo(self.pin)
        if self.size == new_size:
            return
        elif self.size == 'XL' and new_size == 'L':
            servo.value = self.speed
            time.sleep(self.delay * 0.75)
        elif self.size == 'XL' and new_size == 'M':
            servo.value = self.speed
            time.sleep(self.delay * 0.5)
        elif self.size == 'XL' and new_size == 'S':
            servo.value = self.speed
            time.sleep(self.delay * 0.25)
        elif self.size == 'L' and new_size == 'XL':
            servo.value = self.speed
            time.sleep(self.delay * 0.25)
        elif self.size == 'L' and new_size == 'M':
            servo.value = self.speed
            time.sleep(self.delay * 0.75)
        elif self.size == 'L' and new_size == 'S':
            servo.value = self.speed
            time.sleep(self.delay * 0.5)
        elif self.size == 'M' and new_size == 'XL':
            servo.value = self.speed
            time.sleep(self.delay * 0.5)
        elif self.size == 'M' and new_size == 'L':
            servo.value = self.speed
            time.sleep(self.delay * 0.75)
        elif self.size == 'M' and new_size == 'S':
            servo.value = self.speed
            time.sleep(self.delay * 0.25)
        elif self.size == 'S' and new_size == 'XL':
            servo.value = self.speed
            time.sleep(self.delay * 0.25)
        elif self.size == 'S' and new_size == 'L':
            servo.value = self.speed
            time.sleep(self.delay * 0.5)
        elif self.size == 'S' and new_size == 'M':
            servo.value = self.speed
            time.sleep(self.delay * 0.75)

  # Sets pill count
    def setPills(self, added):
        self.pillCount = added

  # Adds pills to pill count
    def addPills(self, added):
        pillCount += added

  # Returns the number of pills in the compartment
    def getPills(self):
        return self.pillCount
  
  # Returns the channel of the motor in the compartment
    def getChannel(self):
        return self.channel
