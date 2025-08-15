from gpiozero import DigitalOutputDevice
from time import sleep
from parameters import params
from motor_run import StepperMotor  # current motor control

def simple_rotate():
    try:
        motor = StepperMotor()


        motor.rotate(steps=24000, step_delay=0.0005, clockwise=False)

    except KeyboardInterrupt:
        print("\nstopped")
    finally:
        motor.cleanup()

if __name__ == "__main__":
    simple_rotate()
