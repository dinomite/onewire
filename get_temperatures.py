#!/usr/bin/env python
# coding=utf-8
from w1thermsensor import W1ThermSensor

for sensor in W1ThermSensor.get_available_sensors():
    print("Sensor %s has temperature %.2f°F" % (sensor.id, sensor.get_temperature(W1ThermSensor.DEGREES_F)))
