# parameters for motor movers


params = {
    'pin':{ # BCM
        'pin_enable'   : 12,
        'pin_step'     : 21,
        'pin_direction': 20
    },
    'device':{
        'stepsize'  : 0.9, #[degree]
        'lead'      : 5 # [mm]
    },
    'motor':{
        'down_speed': 10, # [mm/s]
        'up_speed'  : 0.10, #[mm/s]
        'low_stay'  : 2, # [s] time stay at sinking position
        'high_stay' : 0.5, #[s]
        'repeat'    : 3
    },
    'distance':{
        'distance'  : 10 # [mm] moving distance of sample
    }
}
