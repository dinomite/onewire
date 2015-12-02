# Setup
Install device-tree-compiler

    aptitude install device-tree-compiler

Compile the OneWire init

    dtc -O dtb -o w1-00A0.dtbo -b 0 -@ w1.dts

Link the compiled file to `/lib/firmware`

    sudo ln -sf `pwd`/w1-00A0.dtbo /lib/firmware/

Load the firmware

    echo w1 > /sys/devices/bone_capemgr.9/slots

# Access in Python
Use [w1thermsensor](https://github.com/timofurrer/w1thermsensor)

# References
https://www.adafruit.com/products/374
http://interactingobjects.com/ds18b20-temperature-sensor-on-a-beaglebone-black-running-ubuntu/
http://hipstercircuits.com/dallas-one-wire-temperature-reading-on-beaglebone-black-with-dto/
http://www.bonebrews.com/temperature-monitoring-with-the-ds18b20-on-a-beaglebone-black/
