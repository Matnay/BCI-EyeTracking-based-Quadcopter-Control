import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil
import Tkinter as tk
import os
from time import sleep
import serial
ser = serial.Serial('/dev/ttyACM1',57600)
vehicle = connect("/dev/ttyUSB0", baud = 57600)
time.sleep(6)
print("CONNECTED")
vehicle.mode = VehicleMode("GUIDED")
print("MODE SET TO GUIDED")
reached = False
time.sleep(2)
def arm():
	print("Arming motors")
	while vehicle.armed!=True:
		vehicle.armed = True
		time.sleep(2)

def arm_and_takeoff(altitude):
	arm()
	print("Taking Off")
	vehicle.simple_takeoff(altitude)
	time.sleep(2)
	while True:
		v_alt = vehicle.location.global_relative_frame.alt
		print("Altitude = %.1f m"%v_alt)
		if v_alt >= altitude - 0.1:
			print("Target altitude reached")
			break
		time.sleep(1)
	global reached
	reached = True
	while ser.in_waiting == True:
		var1=ser.readline()
		var1.strip()


  

while True:
	while ser.in_waiting == False:
		pass
	var1=ser.readline()
	var1.strip()
	print (var1)
	var2 = int(var1)
	if var2 > 100 and reached == False:
		vehicle.mode = VehicleMode("GUIDED")
		time.sleep(2)
		arm_and_takeoff(2)
        if ser.in_waiting == True:
            var1=ser.readline()
            var1.strip();
            var2=int(var1)
        if var2>100:
		pass
		print ("continue")
        elif var2<100 and reached==True:		
		print("Mode Set to LAND")
		reached=False
		vehicle.mode = VehicleMode("LAND")
		while vehicle.armed==True:
			time.sleep(1)
			           
            

