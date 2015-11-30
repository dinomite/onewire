# Setup
Install device-tree-compiler

    aptitude install device-tree-compiler

Compile the OneWire init

    dtc -O dtb -o w1-00A0.dtbo -b 0 -@ w1.dts

Link the compiled file to `/lib/firmware`

    sudo ln -sf `pwd`w1-00A0.dtbo /lib/firmware/

Load the firmware

    echo w1 > /sys/devices/bone_capemgr.9/slots
