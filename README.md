# rain-gauge-using-raspberry-pi

Rainfall also known as precipitation is an important part of environment stability. Inorder to have a sustainable echo system, it is important for living beings to have access to clean drinking water. It is also important for early flood warning as well. there are Many efforts to attain this objective depends on accurate precipitation monitoring.This project is an attempt to predict precipitation using davis tipping bucket rain gauge and raspberry pi 4.


Data acquisition devices(DAQs)
    1. Davis AeroCone 6466M Rain Gauge is the mechanical raingauge.
    2. Raspberry Pi as a DAQ device for processing and storing data from davis mechanical raingauge.




Hardware setup
Raspberry pi GPIO 13 and GND pins are connected to two wires from read switch of mechanical rain gauge.
Raspberry pi is powered by a 5v,15ah lithium-ion battery pack.a 100kv solar panel with charge controller is used for recharging.
Data collection is achieved by connecting raspberry pi with a router using ethernet cable.ssh is used for data tranferring  

software setup 
python code in this setup utilizes the Rpi.GPIO library for detecting interrupts. GPIO pin 13 of the Raspberry Pi is set in a pulled-up condition by default, achieved through internal resistors and built-in software functions.the code is designed to detect the rising edge of the interrupt signal. Additionally, we've incorporated a bouncing delay of 50ms to mitigate switch bouncing issues.this code also has a capability of storing data as csv file in 10s inretval.

Working
GPIO pin 13 of the Raspberry Pi is set in a pulled-up condition by default,achieved through internal resistors and built-in software functions.when GPIO 13 pin go to low state as a result of tipping action in davis rain gauge .Our code will detect the interrupt signal and count it.python code covert this counting data to amount of rainfall,and store it as csv file in 10s interval.data stored in rasberry pi can be accessed by ssh protocol.

Error need to be resolved
the bouncing time delay (50ms)provided in the program may result in errors in counting.(ie,when switch is in a closed condition for more than 50ms,)

FAQ
why raspberry pi is choosed instaed of other boards :

Analysed Raspberry Pi audio recording.  Sound files during rain and no rain are clearly differentiable from their spectrogram and does sound different. A benchmark dataset (24 samples/class, 10 sec duration, 32 bit depth) is created.Based upon the simulation conducted, a high bit depth (32 bit float) is suggested for rain/no-rain classification from sound data. Sampling rate as low as 2000 samples/sec found to working fine provided we are using a bit depth of float 32 bit.
 Expored feasibility of Arduino BLE Sense as rain detection  as edge device. The device supports max 16k samples per second at a bit widht of 16 bit signed integer. However ML models requires feature engineering such as FFT or STFT before training and prediction steps. FFT conversion of audio data in BLE Sense was found to be producing overflow errors. The code for the same is attached herewith. As of now, It is suggested to proceed with Raspberry Pi for data collection and model deployment tests.
 
inorder to collect acoustic data we were using arduino.but the sampling rate was not enough for machine learning .so we decided to proceed with rasberry pi which can can provide a high sampling rate compared to arduino.but to train machine learning model we need to compare audio data with davis mechanical rain gauge data.davis rain gauge data was previously taken using arduino and lora.but time stamping issues related to data in lora server. caused problems in data comparison.this is why we desided to move our mechanical rain gauge setup to the same raspberry used for acoustic raingauge. 


 
