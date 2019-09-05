#!/usr/bin/env python
# -*- coding: utf-8 -*-

import commands
import time

__author__ = 'David Qian'

"""
Created on 01/06/2017
@author: David Qian

"""


def fan_control(threshold_on, threshold_off):
    FAN_GPIO = 4

    commands.getoutput('sudo gpio mode %s output' % str(FAN_GPIO))
    commands.getoutput('sudo gpio write %s %s' % (str(FAN_GPIO), '0'))
    print 'stop fan'

    while True:
        cpu_temp = get_temperature()
        if cpu_temp >= threshold_on:
            commands.getoutput('sudo gpio write %s %s' % (str(FAN_GPIO), '1'))
            print 'start fan'

        if cpu_temp < threshold_off:
            commands.getoutput('sudo gpio write %s %s' % (str(FAN_GPIO), '0'))
            print 'stop fan'

        time.sleep(10)


def get_temperature():
    with open('/sys/class/thermal/thermal_zone0/temp') as f:
        cpu_temp_raw = f.read()
        cpu_temp = round(float(cpu_temp_raw)/1000, 1)

    return cpu_temp

if __name__ == '__main__':
    fan_control(60, 50)
