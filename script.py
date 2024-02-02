import RPi.GPIO as GPIO
from datetime import datetime
import time
import csv

interrupt_pin = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(interrupt_pin,GPIO.IN,pull_up_down = GPIO.PUD_UP) 

BUCKET_SIZE = 0.2
count = 0
dt_start = datetime.now()

def bucket_tipped(interrupt_pin):
    print("Bucket Tipped")
    global count
    count += 1
    
def reset_rainfall():
    global count
    count = 0

def saving(dt_now):      
    rainfall = count * BUCKET_SIZE
    file = open("rain_log.csv","a",newline = "")
    tuple = (dt_now,rainfall)
    writer_objt = csv.writer(file)
    writer_objt.writerow(tuple)
    file.close()

GPIO.add_event_detect(interrupt_pin, GPIO.RISING, callback = bucket_tipped,bouncetime = 50)


try:
    while True:      
        dt_now = datetime.now()
        elapsed_time = dt_now - dt_start
        if elapsed_time.seconds % 10 == 0: 
            saving(dt_now)
            time.sleep(1)
            reset_rainfall()  
except KeyboardInterrupt:
    GPIO.cleanup()
    


