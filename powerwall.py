#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import json
import requests
picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic')
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd5in65f
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
from urllib.request import urlopen

logging.basicConfig(level=logging.DEBUG)

try:
    urlDetails = "http://192.168.86.38:8675/aggregates"
    urlBattery = "http://192.168.86.38:8675/soe"
    responseDetails =  requests.get(urlDetails)
    responseBattery =  requests.get(urlBattery)
    powerwallDetails = json.loads(responseDetails.text)
    powerwallBattery = json.loads(responseBattery.text)
    solarpower = str(round(powerwallDetails['solar']['instant_power']/1000, 2))
    sitePower = str(round(powerwallDetails['load']['instant_power']/1000, 2))
    batteryPower = str(round(powerwallDetails['battery']['instant_power']/1000, 2))
    gridPower = str(round(powerwallDetails['site']['instant_power']/1000, 2))
    lastUpdate = str(powerwallDetails['site']['last_communication_time'])[5:19].replace("T"," at ")
    batteryPercentage = round((powerwallBattery['percentage']) / 0.95 - 5/0.95)
    
    if batteryPercentage >= 50 and batteryPercentage <=75:
      batteryColor = 0x00ffff
    elif batteryPercentage > 75: 
      batteryColor = 0x00ff00
    elif batteryPercentage < 50:
      batteryColor = 0x0000ff
     
    logging.info(solarpower)
    
    epd = epd5in65f.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()
    font31 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 31)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    font30 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 50)
    
    logging.info ("Image path: " + os.path.join(picdir, 'background.bmp'))
    Himage = Image.open(os.path.join(picdir, 'background.bmp')) 
    draw = ImageDraw.Draw(Himage)
    draw.text((120, 230), solarpower + ' kW', font = font30, fill = 0)
    draw.text((120, 90), sitePower + ' kW', font = font30, fill = 0)
    draw.text((120, 366), batteryPower + ' kW', font = font30, fill = 0)
    draw.text((120, 500), gridPower + ' kW', font = font30, fill = 0)
    draw.text((52, 12), lastUpdate, font=font31, fill = 0)
    draw.rectangle((340, 588 - 540 * batteryPercentage/100, 405, 588), fill = batteryColor, outline = 0)
    Himage = Himage.rotate(180) 
    epd.display(epd.getbuffer(Himage))
    time.sleep(3)
    
    logging.info("Goto Sleep...")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd5in65f.epdconfig.module_exit()
    exit()
