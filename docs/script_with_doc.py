import RPi.GPIO as GPIO  # GPIO library
from datetime import datetime  # library for real date and time
import csv  # library for data logging

interrupt_pin = 13  # setting  gpio 13 as interrupt pin
GPIO.setmode(GPIO.BCM)  # setting pin numbering to gpio mode(we can also use physical numbering)
GPIO.setup(interrupt_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # setting pin in/out and pulldown/pullup

BUCKET_SIZE = 0.2  # davis rain gauge is calibrated to report 0.2 mm per tip.
count = 0  # for counting tipping
log_count = 0  # for counting data logging
dt_start = datetime.now()  # storing starting date and time


# function to count tipping
def bucket_tipped(interrupt_pin):
    print("Bucket Tipped")
    global count
    count += 1


# function to reset count
def reset_rainfall():
    global count
    count = 0


# function to store data as csv file
def saving(dt_now):
    rainfall = count * BUCKET_SIZE
    file = open("rain_log.csv", "a", newline="")
    tuple = (dt_now, rainfall)
    writer_objt = csv.writer(file)
    writer_objt.writerow(tuple)
    file.close()


GPIO.add_event_detect(interrupt_pin, GPIO.RISING, callback=bucket_tipped, bouncetime=50)
"""Inbuild library function to detect interrupt this function run parellely with other codes in the python file without interrupting them.
so we don't need to invoke this function.switch bouncing time is set to 50ms(its a delay)"""


try:
    while True:  # infinite loop for keeping the code running continuously.this ensure interrupt detection function is always ON.
        dt_now = datetime.now()
        elapsed_time = dt_now - dt_start
        if elapsed_time.seconds % 10 == 0:  # for storing data in every 10s interval
            if log_count == 0:  # to avoid unwanted multiple data logging
                saving(dt_now)
                reset_rainfall()
                log_count = 1
        else:
            log_count = 0
except KeyboardInterrupt:
    GPIO.cleanup()  # cleaning gpio pins when there is a keyboard interrupt (ie,ctrl+c)


# references
# https://www.youtube.com/watch?v=tI6B6BRKU5k&t=596s (bouncing concept)
# https://www.youtube.com/watch?v=T67VfwiJPMg (interrupt reading)
# https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/ (details about RPi.GPIO)
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio-part-3
