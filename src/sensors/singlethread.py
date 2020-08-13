from sensors.motor import motor
from sensors.fan import fan
from sensors.play import music
def singlethread():
    # While server is running
    while(True):
        motor()
        fan()
        music()
    # Once server is closed    
    GPIO.cleanup()        
