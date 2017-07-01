# chickenGuard

Follow the instruction in the guide for # RaspberryPi_TempeartureDS18B20

Build upon a fresh image of Raspbian Lite OS

First:

    $ sudo reboot
    $ sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

    country=DK
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    network={
        ssid="svanevej"
        scan_ssid=1
        psk="Carlsberg1847"
    }
    [CTRL]+[x]
    [y]
    [Enter]
    $ sudo reboot

Next:

    $ sudo nano /boot/config.txt

Go to the bottom of the file, and add this line:

    dtoverlay=w1-gpio

Reboot after saving

    $ sudo reboot

