# supreme-pi
## The Raspberry Pi project

### GPIO Pins

![Pins](http://i.stack.imgur.com/Ct2JG.png)

### VNC

VNC is now avaible in the supreme-pi project. It became real following [this](http://computers.tutsplus.com/tutorials/take-control-of-your-raspberry-pi-using-your-mac-pc-ipad-or-phone--mac-54603) instructions.

1. Change pi password and enable SSH server.
``sudo raspi-config``

2. Get IP address.
``ifconfig``

3. Install VNC.
``sudo apt-get install tightvncserver``
``tightvncserver``

4. On Remmina, server = ``192.168.0.8:1``.

References:

http://jcatala.net/categoria-gnulinux/accediendo-al-escritorio-de-la-raspberry-pi-mediante-vnc

### Physical computing

References:

https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi/basic-photocell-reading

https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/buttons_and_switches/

http://raspberry.io/projects/view/reading-and-writing-from-gpio-ports-from-python/
