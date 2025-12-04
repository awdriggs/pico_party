import time
import board
import pwmio
from digitalio import DigitalInOut, Direction
from adafruit_motor import motor

# Setup IN1 and IN2 as PWM outputs
pwm_in1 = pwmio.PWMOut(board.GP16, frequency=1000, duty_cycle=0)
pwm_in2 = pwmio.PWMOut(board.GP17, frequency=1000, duty_cycle=0)

# Create motor object using PWM
dc_motor = motor.DCMotor(pwm_in1, pwm_in2)

# Motor speed control function (speed ranges from -1.0 to 1.0)
def motor_control(speed):
    dc_motor.throttle = speed

try:
    while True:
        motor_control(0.25)  # Move forward at 50% speed
        time.sleep(2)

        # print("Stopping")
        # motor_control(0)  # Stop motor
        # time.sleep(1)

        # print("Motor Backward at 75% speed")
        # motor_control(-0.75)  # Move backward at 75% speed
        # time.sleep(2)

        # print("Stopping")
        # motor_control(0)  # Stop motor
        # time.sleep(1)

except KeyboardInterrupt:
    print("Stopping motor")
    motor_control(0)

