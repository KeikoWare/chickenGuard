#!/usr/bin/python
import os
import glob
import time
import sys
import datetime
import urllib
import urllib2
import sched 
import RPi.GPIO as GPIO


SwitchButton = 0
SwitchDoor = 1
SwitchPin = [5,13]
SwitchMode = [0,0]

RelayAC = 0
RelayDoor = 1
RelayPin = [24,23]
RelayMode = [0,0]

GPIO.setmode(GPIO.BCM)
GPIO.setup(RelayPin[RelayAC], GPIO.OUT)
GPIO.setup(RelayPin[RelayDoor], GPIO.OUT)
GPIO.output(RelayPin[RelayAC], RelayMode[RelayAC])
GPIO.output(RelayPin[RelayDoor],RelayMode[RelayDoor])

GPIO.setup(SwitchPin[SwitchButton], GPIO.IN, pull_up_down=GPIO.PUD_UP) # HIGH = button released, LOW = button pushed
GPIO.setup(SwitchPin[SwitchDoor], GPIO.IN, pull_up_down=GPIO.PUD_UP) # HIGH = open door, LOW = closed door

def relayOn(relayX):
  RelayMode[relayX] = 1
  if GPIO.input(RelayPin[relayX]) != RelayMode[relayX]:
    GPIO.output(RelayPin[relayX],RelayMode[relayX])

def relayOff(relayX):
  RelayMode[relayX] = 0
  if GPIO.input(RelayPin[relayX]) != RelayMode[relayX]:
    GPIO.output(RelayPin[relayX],RelayMode[relayX])

def toggleRelay(relayX):
  if RelayMode[relayX] == 1 :
    RelayMode[relayX] = 0
  else :
    RelayMode[relayX] = 1
  GPIO.output(RelayPin[relayX],RelayMode[relayX])

my_ONtime_string = "07:00:00"
my_OFFtime_string = "20:30:00"
x = 0

while 1 == 1 :
  time.sleep(0.5)
  i = GPIO.input(SwitchPin[SwitchButton])
  j = GPIO.input(SwitchPin[SwitchDoor])
  x = x + 1
  if i == 0 and SwitchMode[SwitchButton] == 1:
    toggleRelay(RelayDoor)
  SwitchMode[SwitchButton] = i
  SwitchMode[SwitchDoor] = j
  now = datetime.datetime.now()
  my_time = now.strftime("%H:%M:%S")
  light_on = (my_time > my_ONtime_string) and (my_time < my_OFFtime_string) # and SwitchMode[SwitchDoor] == 0
  if light_on :
    relayOn(RelayAC)
  else :
     relayOff(RelayAC)
  print "LightOn ",light_on, " - Button ", i ," - Door ", j , " - AC Relay: ", GPIO.input(RelayPin[RelayAC]), " - Door Relay: ",  GPIO.input(RelayPin[RelayDoor])




