# lens-less-pi
Lens-less Code that runs on the rasperry pi

## Connect on PI
1. Go into same WLAN as the PI. If the PI Top left led blinks red, he has wlan.
2. Connect through SSH:
```
ssh lukasweibel@iot-fbg.local 
```
3. Enter password

## SetUp
1. Git Clone Repository :
```
cd Documents/
git clone https://github.com/GsteigerDominik/lens-less-pi.git
```
2. Install GPSD Requirements
```
cd lens-less-pi/src/
sudo apt-get install gpsd gpsd-clients
sudo apt-get install gps3
```

3. Autostart configs hinterlegen
```
crontab -e

@reboot python /home/lukasweibel/Documents/lens-less-pi/src/wlan_gps_status.py
@reboot python /home/lukasweibel/Documents/lens-less-pi/src/main.py

sudo reboot
```

## API Definition
```
{
  "latitude": float,
  "longitude": float,
  "temperature": float,
  "brightness": number(0-6),
  "population": number(0-6),
  "colorscheme": "string(blackwhite,colourfull)",
  "style": "string(realistic,futuristic,vintage,drawing)"
}```

## References
1. GPS Module: https://wiki.dfrobot.com/USB_GPS_Receiver_SKU_TEL0137
2. GPS Setup: https://maker.pro/raspberry-pi/tutorial/how-to-read-gps-data-with-python-on-a-raspberry-pi