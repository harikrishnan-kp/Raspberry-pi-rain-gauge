

## RPi.GPIO installation
The RPi.GPIO module is installed by default in Raspbian. To make sure that it is at the latest version:
```bash
sudo apt-get update
sudo apt-get install python-rpi.gpio python3-rpi.gpio
```
Other Distributions
It is recommended that you install RPi.GPIO using the pip utility as superuser (root):it ensure that the library is installed system-wide and accessible to all users.
```bash
sudo pip install RPi.GPIO
```
OR
```bash
sudo pip3 install RPi.GPIO 
```
### NOTE
If there is an GPIO error says   "error: failed to add edge detection.you need to install the following dependencies if there is an error named as failed to add egde detection." try the following commands 

```bash     
sudo apt-get install python3-rpi.gpio
pip install lgpio==0.0.0.2
ls -l /sys/class/gpio/
sudo chmod 777 /sys/class/gpio/export 
sudo echo 6 > /sys/class/gpio/export 
ls /sys/class/gpio/
ls -l /sys/class/gpio/gpio6/ 
sudo chmod 777 /sys/class/gpio/gpio6/direction 
sudo echo in > /sys/class/gpio/gpio6/direction 
ls -l /sys/class/gpio/gpio6/direction 
ls -l /sys/class/gpio/gpio6/edge 
sudo chmod 777 /sys/class/gpio/gpio6/edge
```



## influxdb-client installation
if we are installing rasbian os 64 bit
pip install influxdb-client won't work.they will recomment to try using apt.but apt doesnot contain the package influxdb-cleint.so we need to create a virtual environment for installing influxdb client.

if the OS is ubuntu server os 22.04.4
```bash
pip install influxdb client
```

