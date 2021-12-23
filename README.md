# Tollhouse

This is a Flask web application that front ends a Raspberry Pi. The On button turns the RGB LED on, which flashes back and forth between Red and Green (Merry Christmas!). The off button, naturally stops the lights.

The GPIO control currently requires **_root level permissions_**, which means the web application currently **_runs as root_**. Do not run this in production until you figure out how to **_run using a least privilege_** account. Yes you, I haven't figured it out yet.<br><br>
The RGB LED is a [Keyes LED RGB](https://arduinomodules.info/ky-016-rgb-full-color-led-module/) module. There are two different versions of this module, one of them is a dome shaped LED which is not as bright as it has a white cover over the LED.<br>


The GPIO pinout is:<br>
GND - Pin 9<br>
Red - Pin 11<br>
Green - Pin 13<br>
Blue - Not used
