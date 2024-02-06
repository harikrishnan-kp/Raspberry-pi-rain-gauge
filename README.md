﻿# rain-gauge-using-raspberry-pi

Rainfall also known as precipitation is an important part of environment stability.Rain gauges are indispensable tools for monitoring and managing precipitation, which has significant implications for weather forecasting, water resource management, flood prediction, agriculture, climate studies and various other fields and activities.There are Many efforts to attain accurate precipitation monitoring and analysis.This project is an attempt to estimate precipitation using davis tipping bucket rain sensor and raspberry pi-4.This project aims at producing locally maintainable rain gauge while ensuring accurate and dependable results.


### Data acquisition devices(DAQs)
1. [Davis AeroCone 6466M](https://www.amazon.de/-/en/Davis-AeroCone-6466M-Gauge-Sensor/dp/B08629NFVG) is the mechanical raingauge.
2. Raspberry Pi 4 model B as a DAQ device for processing and storing data from davis mechanical raingauge.

<img src="https://m.media-amazon.com/images/I/612KqYGrL7L._AC_SX466_.jpg" height="300"/>      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Raspberry_Pi_4_Model_B_-_Side.jpg/1200px-Raspberry_Pi_4_Model_B_-_Side.jpg" alt="raspberrypi" width="350"/>

## Hardware setup
Raspberry pi GPIO 13 and GND pins are connected to two wires from read switch of davis mechanical rain gauge.Raspberry pi is powered by a 5v,15ah lithium-ion battery pack.a 100w solar panel with charge controller is used for recharging.Data collection is achieved by connecting raspberry pi with a nearby router using ethernet cable(we can also use wifi for connecting to router).secure shell (SSH) protocol is used for transferring data to our computer system.   

<img src="https://github.com/Thelastblackpearl/rain-gauge-using-raspberry-pi/blob/be1930543c1d64de2b89c4dc69c4965bb87f0bd6/docs/hardware%20setup%201.jpg"  width ="500">

### Software setup 
python code in this setup utilizes **Rpi.GPIO** library for detecting interrupts.GPIO pin 13 of the Raspberry Pi is set in a pulled-up condition by default, achieved through internal resistors and built-in software functions.the code is designed to detect the rising edge of the interrupt signal. Additionally, we've incorporated a bouncing delay of 50ms to mitigate switch bouncing issues.this code also has a capability of storing data as csv file in 10s inretval.

### Working
GPIO pin 13 of the Raspberry Pi is set in a pulled-up condition by default,achieved through internal resistors and built-in software functions.when GPIO 13 pin changes to low state as the result of tipping action(closing read switch) in davis rain gauge.Our code will detect the interrupt signal.python code will count number of interrupt signal and convert this data to amount of rainfall,and store it as csv file in 10s interval.data stored in rasberry pi can be accessed by ssh protocol.

### Limitations
This rain gauge has the following limitations.
* **Accuracy:** Tipping bucket rain gauges may not always provide accurate measurements, especially during heavy rainfall events or in windy conditions. Splashing or wind-driven rain can lead to inaccuracies in measurement.
* **Underestimation of Intense Rainfall:** During intense rainfall, the tipping bucket mechanism may not be able to keep up with the rapid influx of water, leading to underestimation of rainfall amounts.
* **Evaporation Losses:** Tipping bucket rain gauges are susceptible to evaporation losses, especially in warm and windy conditions.
* **Maintenance Requirements:** Tipping bucket rain gauges require regular maintenance to ensure accurate measurement.
* **Freezing and Snow Accumulation:** In cold climates, freezing temperatures and snow accumulation can interfere with the operation of tipping bucket rain gauges.
Despite these limitations, tipping bucket rain gauges remain valuable tools for monitoring rainfall in many applications

### Error need to be resolved
The bouncing time delay (50ms)provided in the program may result in errors in counting(ie,when switch is in a closed condition for more than 50ms).possibility of this error need to be examined and resolved.

### future updates
Data logging feature need to improved,as of now it is difficult to take desired data when there is alot of data.data logging must be structured based on days,hour for easy accessing data.

### FAQ
why raspberry pi is choosed instaed of other boards as DAQ: our icfoss R&D team was working on a acoustic rain gauge using machine learning technology.machine learning model was teached by comparing data collected from acoustic DAQ setup and davis mechanical rain guage.Both data gathering setup were using arduino as processing unit.but sampling rate of arduino was not enough for training ML model,To compensate the issue we switched our sound data gathering system to raspberry pi-4 which can provide high sampling rate compared to arduino.inorder to make data comparison easy and to resolve issues related to timestamping, davis rain gauge is also moved to raspberry pi DAQ.
