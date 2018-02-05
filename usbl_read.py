#!/usr/bin/env python
import serial
ser = serial.Serial('/dev/ttyUSB0', 19200)

while True:
	line = ser.readline()
	if line:
		data_list = line.split(",")
		for data in data_list:
			print data
