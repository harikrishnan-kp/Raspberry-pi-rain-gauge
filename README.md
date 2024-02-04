# rain-gauge-using-raspberry-pi

Rainguages are mainly attached in association with weather station for monitoring weather parameter in a regular bias. The advantage of long time of rain data can be used for data analysis in terms for prediction of rainfall and alerts in case of heavy or rain fall.Rainfall also known as precipitation is an important part of environment stability. Inorder to have a sustainable echo system, it is important for living beings to have access to clean drinking water. It is also important for early flood warning as well. there are Many efforts to attain this objective depends on accurate precipitation monitoring.This project is an attempt to predict precipitation using davis tipping bucket rain gauge and raspberry pi 4.This project aims at producing locally maintainable rain gauge at cheaper cost while ensuring accurate and dependable results.


### Data acquisition devices(DAQs)
1. [Davis AeroCone 6466M](https://www.amazon.de/-/en/Davis-AeroCone-6466M-Gauge-Sensor/dp/B08629NFVG) is the mechanical raingauge.
2. Raspberry Pi 4 model B as a DAQ device for processing and storing data from davis mechanical raingauge.

<img src="https://m.media-amazon.com/images/I/612KqYGrL7L._AC_SX466_.jpg" height="300"/>      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Raspberry_Pi_4_Model_B_-_Side.jpg/1200px-Raspberry_Pi_4_Model_B_-_Side.jpg" alt="raspberrypi" width="350"/>

## Hardware setup
Raspberry pi GPIO 13 and GND pins are connected to two wires from read switch of davis mechanical rain gauge.
Raspberry pi is powered by a 5v,15ah lithium-ion battery pack.a 100w solar panel with charge controller is used for recharging.
Data collection is achieved by connecting raspberry pi with a nearby router using ethernet cable.
secure shell (SSH) protocol is used for transferring data to our system.   

<img src="https://github.com/Thelastblackpearl/rain-gauge-using-raspberry-pi/blob/ac7802241a44cf78f27233e284e040065e3c8561/docs/hardware%20setup.jpg"  width ="500">

### Software setup 
python code in this setup utilizes Rpi.GPIO library for detecting interrupts.GPIO pin 13 of the Raspberry Pi is set in a pulled-up condition by default, achieved through internal resistors and built-in software functions.the code is designed to detect the rising edge of the interrupt signal. Additionally, we've incorporated a bouncing delay of 50ms to mitigate switch bouncing issues.this code also has a capability of storing data as csv file in 10s inretval.

### Working
GPIO pin 13 of the Raspberry Pi is set in a pulled-up condition by default,achieved through internal resistors and built-in software functions.when GPIO 13 pin changes to low state as the result of tipping action(closing read switch) in davis rain gauge.Our code will detect the interrupt signal.python code will count number of interrupt signal and convert this data to amount of rainfall,and store it as csv file in 10s interval.data stored in rasberry pi can be accessed by ssh protocol.

### Limitations
This rain gauge has all the limitations of a mechanical raingauge 

### Error need to be resolved
the bouncing time delay (50ms)provided in the program may result in errors in counting.(ie,when switch is in a closed condition for more than 50ms,)

### FAQ
why raspberry pi is choosed instaed of other boards : our icfoss R%D team was working on a acoustic rain gauge using machine learning technology.machine learning model was teached by comparing data collected from a mic and davis rain guage.both data gathering setup were using arduino as processing unit.but sampling rate of arduino was not enough for training ml model, so we switched our sound data gathering system to to raspberry pi which can provide high sampling rate compared to arduino.inorder to make data comparison easy and to resolve timestamping issues davis rain gauge is also moved to raspberry pi



 
