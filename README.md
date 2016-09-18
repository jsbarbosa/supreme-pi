# supreme-pi
## The Raspberry Pi project

### GPIO Pins
<img src="http://i.stack.imgur.com/Ct2JG.png" width="500">

### VNC

VNC is now avaible in the supreme-pi project. It became real following [this](http://computers.tutsplus.com/tutorials/take-control-of-your-raspberry-pi-using-your-mac-pc-ipad-or-phone--mac-54603) instructions.

1. Change pi password and enable SSH server.
``sudo raspi-config``

2. Get IP address.
``ifconfig``

3. Install VNC.
``sudo apt-get install tightvncserver``
``tightvncserver``

It might be easier to use the Raspberry using an Ethernet cable. On Ubuntu (host):
> Edit Connections.. > Ethernet Wired connection 1 > Edit > IPv4 Settings > Method "Shared to other computers"

4. To reveal IP address
``arp -e | grep enp3s0``

5. On Remmina, server = ``192.168.0.8:1``.

References:

http://jcatala.net/categoria-gnulinux/accediendo-al-escritorio-de-la-raspberry-pi-mediante-vnc

### Physical computing

References:

https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi/basic-photocell-reading

https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/buttons_and_switches/

http://raspberry.io/projects/view/reading-and-writing-from-gpio-ports-from-python/
