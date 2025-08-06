from gpiozero import DigitalOutputDevice
from time import sleep
from parameters import params



# Pin Definitions (using BCM numbering)
enable_pin = params['pin']['pin_enable']
step_pin = params['pin']['pin_step']
dir_pin = params['pin']['pin_direction']



class StepperMotor:
    def __init__(self):

        # Initialize GPIO devices
        self.enable = DigitalOutputDevice(enable_pin, active_high=False) # original False
        self.step = DigitalOutputDevice(step_pin)
        self.direction = DigitalOutputDevice(dir_pin)

        # Enable the driver (active low, so setting to True enables)
        self.enable.on()

    def rotate(self, steps, step_delay, clockwise=True): # original 0.0008
        """Rotate the motor a specified number of steps"""
        self.direction.value = clockwise  # Set direction
        for _ in range(steps):
            self.step.on()
            sleep(step_delay/2)
            self.step.off()
            sleep(step_delay/2)

    def cleanup(self):
        """Clean up GPIO resources"""
        self.enable.off()  # Disable the driver
        self.enable.close()
        self.step.close()
        self.direction.close()

def main():
    try:

        motor = StepperMotor()

        # device
        stepsize = params['device']['stepsize']
        lead     = params['device']['lead']


        # the movement
        dis     = params['distance']['distance']
        v_down  = params['motor']['down_speed']
        v_up    = params['motor']['up_speed']
        t_sink  = params['motor']['low_stay']
        t_top   = params['motor']['high_stay']
        repeat  = params['motor']['repeat']

        step            = int(360*dis/lead/stepsize)
        step_delay_down = lead*stepsize/360/v_down
        step_delay_up   = lead*stepsize/360/v_up
        print(step, step_delay_down, step_delay_up)



        for i in range(repeat):
            # Rotate clockwise
            motor.rotate(step, step_delay_down, clockwise=True)
            sleep(t_sink)

            # Rotate counter-clockwise
            motor.rotate(step, step_delay_up, clockwise=False)
            sleep(t_top)
            print("one cycle finished")

    except KeyboardInterrupt:
        print("\nProgram stopped by user")
    finally:
        motor.cleanup()

if __name__ == "__main__":
    main()
