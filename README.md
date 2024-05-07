# lens-less-pi
Lens-less Code that runs on the rasperry pi

#GPS Module
https://wiki.dfrobot.com/USB_GPS_Receiver_SKU_TEL0137


https://maker.pro/raspberry-pi/tutorial/how-to-read-gps-data-with-python-on-a-raspberry-pi


#REQUIRENMENTS
sudo apt-get install gpsd gpsd-clients

#CRONTAB um beim start zu
crontab -e
@reboot python /home/lukasweibel/Documents/blink.py

@reboot rm -rf repository-name
@reboot git clone https://github.com/username/repository-name