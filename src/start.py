# Threading Imports
import threading
from time import sleep
import time
from src.controllers.statusLcd import lcd 
from src.controllers.sound import sound
from src.controllers.singlethread import singlethread

# Creating the single thread
singlethread = threading.Thread(target=singlethread, daemon=True)
singlethread.start()

# Creating the status thread
lcdStatusThread = threading.Thread(target=lcd, daemon=True)
lcdStatusThread.start()
#
soundThread = threading.Thread(target=sound, daemon=True)
soundThread.start()
