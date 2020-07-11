import os
import settings
from threading import Timer

def compute_orders(pumps):
    if(len(pumps) == 0): 
        print('there is not pumps specified')
        return
        
    # we sort the order to get the greatter duration
    sorted_pumps = tuple(sorted(pumps, key=lambda pump: pump[1]))
    # we get the greatest duration to have the total duration of the shaking
    shaking_duration = sorted_pumps[-1][1]

    start_shaking()
    # we start the timer for each pump
    for pump in sorted_pumps:
        activate_pump(pump[0])
        r = Timer(pump[1], stop_pump, [pump[0]])
        r.start()
    # we set a timer for the end of shaking
    Timer(shaking_duration, stop_shaking).start()
    
def start_shaking():
    # here we can start the led
    print('shaking begins')
    for initCmd in settings.relay_init:
        print(initCmd)

def activate_pump(pump_nb):
    print('start pump %d' % pump_nb)
    # execute the gpio command (ex:'gpio write 0 0')
    #os.system(settings.relay_cmd[pump_nb] % 0)
    print(settings.relay_cmd[pump_nb] % True)

def stop_pump(pump_nb):
    print('stop pump %d' % pump_nb)
    # execute the gpio command (ex:'gpio write 0 1')
    #os.system(settings.relay_cmd[pump_nb] % 1)
    print(settings.relay_cmd[pump_nb] % False)

def stop_shaking():
    # here we can stop the led
    print('shaking is over')