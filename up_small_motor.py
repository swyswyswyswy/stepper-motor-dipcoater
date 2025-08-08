from gpiozero import DigitalOutputDevice
from time import sleep
from parameters import params
from motor_run import StepperMotor  # import current motor_control class

def simple_rotate():
    try:
        motor = StepperMotor()

       
        motor.rotate(steps=80, step_delay=0.001, clockwise=True)
        
    except KeyboardInterrupt:
        print("\nstopped")
    finally:
        motor.cleanup()

if __name__ == "__main__":
    simple_rotate()
