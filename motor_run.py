from gpiozero import DigitalOutputDevice
from time import sleep
from parameters import params
from move_params import move_params


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
        dis        = move_params['move']['distance']
        v_down     = move_params['move']['down_speed']
        v_up       = move_params['move']['up_speed']
        t_sink     = move_params['move']['low_stay']
        t_top      = move_params['move']['high_stay']
        start_pt   = move_params['move']['start_point']
        returnback = move_params['move']['returnback']
        repeat     = move_params['move']['repeat']


        step            = int(360*dis/lead/stepsize)
        step_delay_down = lead*stepsize/360/v_down
        step_delay_up   = lead*stepsize/360/v_up
        print(step, step_delay_down, step_delay_up)


        if start_pt.lower() == 'top':
            phase1 = False
            phase2 = True
            t1 = t_sink
            t2 = t_top
        else:
            phase1 = True
            phase2 = False
            t1 = t_top
            t2 = t_sink

        for i in range(repeat):
            # Rotate counter-clockwise, going down
            motor.rotate(step, step_delay_down, clockwise = phase1)
            sleep(t1)

            # Rotate clockwise, going up
            motor.rotate(step, step_delay_up, clockwise = phase2)
            sleep(t2)
            print("one cycle finished")

    except KeyboardInterrupt:
        print("\nProgram stopped by user")
    finally:
        motor.cleanup()

if __name__ == "__main__":
    main()
