![alt text](https://github.com/rog0978/powerwall_display/blob/main/display.jpg?raw=true)
# Tesla Powerwall Desktop Model with e-Paper display
This is a quick and dirty overview on my model-Powerwall that is displaying stats of my solar / battery system on a color e-paper display. It gets refreshed every 10 minutes (can be changed of course) - just keep in mind that the display takes about 25 seconds to fully refresh :)

## Pre-conditions

Besides the material listed below, your powerwall needs to be connected to your local network (Wifi or wired) from which you plan to connect the display to.
Also, this assumes basic knowledge on how to setup and operate a Raspi Pi (e.g. how to install Raspi OS in a headless way so it can be connected to via SSH)

## Hardware used

* Display: https://www.waveshare.com/5.65inch-e-paper-module-f.htm
* Raspberry Pi (I am using a Zero W, but any other version with Wifi connectivity should work): https://www.raspberrypi.com/products/raspberry-pi-zero-w/
* Black & white acrylic for the case (any source, the svg files provided here are made for 3.8mm thick material, adjust the files for your material if necessary)

## Software setup

### 3. Set up Raspberry Pi

Install a standard Raspi OS (I am using Raspberry Pi OS lite), there are tons of instructions out there. One of them here: https://www.raspberrypi.com/software/operating-systems/

### 4. Installation of Powerwall Proxy

Once the basic stuff in installed, install below proxy via docker (manages all requests to the local Powerwall API in a neat and easy way)

https://github.com/jasonacox/pypowerwall/tree/main/proxy

### 5. Installation of e-Paper Display drivers

Use this guide to install necessary (python3) libraries, as well as to get instructions on how to connect the display to the Pi: https://www.waveshare.com/wiki/5.65inch_e-Paper_Module_(F)#Hardware_connection

### 6. Clone this repository to your Pi

* `$ git clone https://github.com/rog0978/powerwall_display.git`
* in powerwall.py, replace the IP address with your IP address assigned to your Pi for variables "urlDetails" & "urlBattery"
* you can test if everything works by running `$sudo ./powerwall.sh`

### 7. Set up the display script to run every 10 minutes between 7am and 7pm

`$ sudo crontab -e`

Add the following line at the end of the file and save afterwards: 

## Creating the Powerwall model

The svg files for laser cutting are in the "case" folder. I also added pdf versions which are true to dimensions (if you material is more or less the same thickness of 3.8mm like the one I used). Measure your material first and then make changes to the svg source files if necessary.
For the Tesla logo, I engrave that part and then spray-paint it while the masking tape is still on the Acrylic. Alternatively, painting it with a brush will also work (keeping the masking tape on will drastically simplify this ;-) )
