import RPi.GPIO as GPIO
from datetime import datetime
import csv
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

interrupt_pin = 13
GPIO.setmode(GPIO.BCM) # setting pin numbering to gpio mode(we can also use physical numbering)
GPIO.setup(interrupt_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

BUCKET_SIZE = 0.2  # davis rain gauge is calibrated to report 0.2 mm per tip.
count = 0  # tipping counter
log_count = 0
dt_start = datetime.now()


# to count tipping
def bucket_tipped(interrupt_pin):
    # print("Bucket Tipped")
    global count
    count += 1


# to reset count
def reset_rainfall():
    global count
    count = 0


# to store data as csv file
def saving(dt_now):
    rainfall = count * BUCKET_SIZE
    # print(rainfall)
    file = open("rain_log.csv", "a", newline="")
    tuple = (dt_now, rainfall)
    writer_objt = csv.writer(file)
    writer_objt.writerow(tuple)
    file.close()


# for writing data to influxdb
def influxdb() -> bool:
    rain = count * BUCKET_SIZE
    # Configure influxDB credentials 
    bucket = "<bucket name>" 
    org = "<org name>"      
    token = "<token>"
    url= "<url of DB>"

    client = influxdb_client.InfluxDBClient(url=url,token=token,org=org)
    write_api = client.write_api(write_options=SYNCHRONOUS)
    p = influxdb_client.Point("rainfall").tag("location","some where on earth").field("rain in mm",rain)
    write_api.write(bucket=bucket, org=org, record=p)
    client.close()
    return True


GPIO.add_event_detect(interrupt_pin, GPIO.RISING, callback=bucket_tipped, bouncetime=50)
"""Inbuild library function to detect interrupt this function run parellely with other codes in the python file without interrupting them.
so we don't need to invoke this function.switch bouncing time is set to 50ms(its a delay)"""


try:
    while True:
        dt_now = datetime.now()
        elapsed_time = dt_now.minute - dt_start.minute
        if elapsed_time % 5 == 0:
            if log_count == 0: # to avoid unwanted multiple data logging
                saving(dt_now)
                influxdb()
                reset_rainfall()
                log_count = 1
        else:
            log_count = 0
except KeyboardInterrupt:
    GPIO.cleanup()
    