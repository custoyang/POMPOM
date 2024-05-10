import time
from adafruit_servokit import ServoKit

# Setup PCA9685 module
kit = ServoKit(channels=16)

# Define channels for the servos
channel_4 = 4
channel_5 = 6

def control_servo(channel, action):
    """Control the servo's movement."""
    if action == "stop":
        # Stop the servo by sending a neutral pulse (about 90 degrees in standard servos)
        kit.servo[channel].angle = 90
    elif action == "clockwise":
        # Rotate clockwise (you might need to adjust the value slightly less than 90)
        kit.servo[channel].angle = 85
    elif action == "counterclockwise":
        # Rotate counterclockwise (you might need to adjust the value slightly more than 90)
        kit.servo[channel].angle = 95

    print(f"Servo on channel {channel} set to {action}.")

def main():
    try:
        # Rotate servo on channel 4 clockwise
        control_servo(channel_4, "clockwise")
        time.sleep(2)  # Spin for 2 seconds

        # Stop servo on channel 4
        control_servo(channel_4, "stop")
        time.sleep(1)  # Stop for 1 second

        # Rotate servo on channel 4 counterclockwise
        control_servo(channel_4, "counterclockwise")
        time.sleep(2)  # Spin for 2 seconds

        # Stop servo on channel 4
        control_servo(channel_4, "stop")
        time.sleep(1)  # Stop for 1 second

        # Repeat the same for channel 5
        control_servo(channel_5, "clockwise")
        time.sleep(2)
        control_servo(channel_5, "stop")
        time.sleep(1)
        control_servo(channel_5, "counterclockwise")
        time.sleep(2)
        control_servo(channel_5, "stop")

        print("Demo complete. Both servos returned to stop position.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
