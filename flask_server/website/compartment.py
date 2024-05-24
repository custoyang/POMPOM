from gpiozero import Servo
from flask import current_app
from flask_login import current_user
from website import db
from .models import Pills, User
from datetime import datetime
import time

class Compartment:
    def __init__(self, pill_id):
        with current_app.app_context():
            pill = db.session.query(Pills).filter_by(compartment=pill_id).first()
            self.pin = self.setPin(pill.compartment)
            self.pillCount = pill.amount
            self.pill = pill.name
            self.frequency = pill.frequency # in hours
            self.size = pill.size
            self.delay = 2.7
            self.speed = 0.075
            if self.pin == 12:
                self.delay = 1.6
                self.speed = 0.1125
            if self.pin == 19:
                self.delay = 1.5
                self.speed = 0.1125
            self.servo = Servo(self.pin)
            self.servo.value = None
            self.rotated = False
    
    def rotate_once(self):
        self.rotated = True
        self.servo.value = self.speed
        time.sleep(self.delay)
        self.servo.value = None
        time.sleep(self.delay)

    
    def calibration(self, new_size):
        low = 0.16
        med = 0.45
        high = 0.715
        if self.size == new_size:
            return
        elif self.size == 'XL' and new_size == 'L':
            self.servo.value = self.speed
            time.sleep(self.delay * low)
        elif self.size == 'XL' and new_size == 'M':
            self.servo.value = self.speed
            time.sleep(self.delay * med)
        elif self.size == 'XL' and new_size == 'S':
            self.servo.value = self.speed
            time.sleep(self.delay * high)
        elif self.size == 'L' and new_size == 'XL':
            self.servo.value = self.speed
            time.sleep(self.delay * low)
        elif self.size == 'L' and new_size == 'M':
            self.servo.value = self.speed
            time.sleep(self.delay * high)
        elif self.size == 'L' and new_size == 'S':
            self.servo.value = self.speed
            time.sleep(self.delay * med)
        elif self.size == 'M' and new_size == 'XL':
            self.servo.value = self.speed
            time.sleep(self.delay * med)
        elif self.size == 'M' and new_size == 'L':
            self.servo.value = self.speed
            time.sleep(self.delay * high)
        elif self.size == 'M' and new_size == 'S':
            self.servo.value = self.speed
            time.sleep(self.delay * low)
        elif self.size == 'S' and new_size == 'XL':
            self.servo.value = self.speed
            time.sleep(self.delay * low)
        elif self.size == 'S' and new_size == 'L':
            self.servo.value = self.speed
            time.sleep(self.delay * med)
        elif self.size == 'S' and new_size == 'M':
            self.servo.value = self.speed
            time.sleep(self.delay * high)
        self.servo.value = None

  # Sets pill count
    def setPills(self, added):
        self.pillCount = added

  # Adds pills to pill count
    def addPills(self, added):
        self.pillCount += added

  # Returns the number of pills in the compartment
    def getPills(self):
        return self.pillCount
  
    def setPin(compartment_id):
        if compartment_id == 1:
            return 12
        elif compartment_id == 2:
            return 13
        elif compartment_id == 3:
            return 18
        elif compartment_id == 4:
            return 19

def background_task(app):
    with app.app_context():
        # if current_user.is_authenticated:
        check_and_dispense()
        time.sleep(10)

def check_and_dispense():
    print('helloooooooooooo')
    now = datetime.now()

    # Zero out seconds (and microseconds for completeness)
    rounded_time = now.replace(second=0, microsecond=0)
    # Format to string with zeroed seconds
    current_time = rounded_time.strftime('%H:%M:%S')
    print(current_time)
    pills_to_dispense = db.session.query(Pills).filter_by(dispense_time=current_time).all()
    print(pills_to_dispense)
    # pills_to_dispense = db.session.query(Pills).filter_by(user_id=current_user.id, dispense_time=current_time).all()
    for pill in pills_to_dispense:
        compartment = Compartment(pill.compartment)
        if compartment.rotated == True:
            compartment.rotate_once()
        elif compartment.rotated == False:
            compartment.calibration(pill.size)
        print(f"Dispensed pill from pin {compartment.pin}")

def dispense():

    compartment = Compartment(pill.compartment)
    if compartment.rotated == True:
        compartment.rotate_once()
    elif compartment.rotated == False:
        compartment.calibration(pill.size)

