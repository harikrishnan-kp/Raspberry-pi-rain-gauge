

## RPi.GPIO installation
The RPi.GPIO module is installed by default in Raspbian. To make sure that it is at the latest version:
```bash
sudo apt-get update
sudo apt-get install python-rpi.gpio python3-rpi.gpio
```
Other Distributions
It is recommended that you install RPi.GPIO using the pip utility as superuser (root): it ensure that the library is installed system-wide and accessible to all users.
```bash
sudo pip install RPi.GPIO
```
OR
```bash
sudo pip3 install RPi.GPIO 
```
OR
```bash
sudo apt-get install python3-rpi.gpio 
```
### NOTE
If there is an GPIO error "error: failed to add edge detection".reboot your device 

```bash     
sudo reboot
```



## influxdb-client installation
if we are installing rasbian os 64 bit
pip install influxdb-client won't work.they will recomment to try using apt.but apt doesnot contain the package influxdb-cleint.so we need to create a virtual environment for installing influxdb client.

if the OS is ubuntu server os 22.04.4
```bash
pip install influxdb client
```


