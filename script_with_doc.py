import RPi.GPIO as GPIO                                       # GPIO library
from datetime import datetime                                 # library for real date and time
import time                                                   # library to provide sleep
import csv                                                    # library for data logging

interrupt_pin = 13                                            # setting gpio 13 as interrupt pin
GPIO.setmode(GPIO.BCM)                                        # setting pin numbering to gpio mode(we can also use physical numbering)
GPIO.setup(interrupt_pin,GPIO.IN,pull_up_down = GPIO.PUD_UP)  # setting pin in/out and pulldown/pullup

BUCKET_SIZE = 0.2                                             # davis rain gauge is calibrated to report 0.2 mm per tip.
count = 0                                                     # for counting tipping
dt_start = datetime.now()                                     # storing starting date and time

def bucket_tipped(interrupt_pin):                             # function to count tipping
    print("Bucket Tipped")
    global count
    count += 1
    
def reset_rainfall():                                         # function to reset count
    global count
    count = 0

def saving(dt_now):                                           # function to store data as csv file
    rainfall = count * BUCKET_SIZE 
    file = open("rain_log.csv","a",newline = "")
    tuple = (dt_now,rainfall)
    writer_objt = csv.writer(file)
    writer_objt.writerow(tuple)
    file.close()
  
GPIO.add_event_detect(interrupt_pin, GPIO.RISING, callback = bucket_tipped,bouncetime = 50) # inbuild library function to detect interrupt.
                                                                                            # this function run parellely with other codes in 
                                                                                            # the python file without interrupting them.so we 
                                                                                            # don't need to invoke this function.
                                                                                            # switch bouncing time is set to 50ms(its a delay)

try:
    while True:                   # infinite loop for keeping the code running continuously.this ensure interrupt detection function is always ON. 
        dt_now = datetime.now()
        elapsed_time = dt_now - dt_start
        if elapsed_time.seconds % 10 == 0:                                                  # for storing data in every 10s interval
            saving(dt_now)
            time.sleep(1)             # sleep is added to avoid multiple data storing when when if condition is satisfied for a period of 1second
            reset_rainfall()  
except KeyboardInterrupt:
    GPIO.cleanup()                                                            # cleaning gpio pins when there is a keyboard interrupt (ie,ctrl+c)
    
    
    
    
#references
# https://www.youtube.com/watch?v=tI6B6BRKU5k&t=596s (bouncing concept)
# https://www.youtube.com/watch?v=T67VfwiJPMg (interrupt reading)
# https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/ (details about RPi.GPIO)
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio-part-3 

