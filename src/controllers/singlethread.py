from src.controllers.motor import motor
from src.controllers.fan import fan
from src.controllers.play import music
def singlethread():
    # While server is running
    while(True):
        motor()
        fan()
        music()
    # Once server is closed    
    # GPIO.cleanup()        
