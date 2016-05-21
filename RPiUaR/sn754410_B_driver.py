
# driver program for sn754410

from time import sleep #We will need to sleep the code at points
import RPi.GPIO as GPIO #Import the GPIO library as GPIO
import signal
import sys

#Setup GPIO
GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False) # Ignore any errors

sleeptime = 6

GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)


def forward():
        print "forward"
        GPIO.output(11,1)
        GPIO.output(13,0)

def backwards():
        print "backwards"
        GPIO.output(11,0)
        GPIO.output(13,1)
        
def stop():
        print "stop"
        GPIO.output(11,0)
        GPIO.output(13,0)

def breakhandler(signum,frame):
        print "goodbye"
        stop()
        GPIO.cleanup
        sys.exit()

signal.signal(signal.SIGINT,breakhandler)

while True:
        forward()
        sleep(sleeptime)
        stop()
        backwards()
        sleep(sleeptime)
        stop()
