#!/usr/bin/python
import urllib
import urllib2
import json
from time import sleep
from pprint import pprint
import RPi.GPIO as GPIO


deviceName = "The Goggel Pi"
deviceDescription ="The best goggel-place in the world."
deviceId = ""
message = ""
action = "" 
urlStatus = "https://www.keikoware.dk/rpi/status/"
urlQueue = "https://www.keikoware.dk/rpi/queue/"

SwitchButton = 0
SwitchDoor = 1
SwitchPin = [5,13]
SwitchHold = [0,0]

RelayAC = 0
RelayDoor = 1
RelayPin = [23,24]
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
  GPIO.output(RelayPin[relayX],RelayMode[relayX])


def relayOff(relayX):
  RelayMode[relayX] = 0
  GPIO.output(RelayPin[relayX],RelayMode[relayX])


def toggleRelay(relayX):
  if RelayMode[relayX] :
    RelayMode[relayX] = 0
  else :
    RelayMode[relayX] = 1


def getserial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"

  return cpuserial

def initialize():
  global deviceId
  global message
  payload = {"deviceId": getserial() ,"action":"get"}
  request = urllib2.Request(url,data=urllib.urlencode(payload))
  request.add_header('Content-Type','application/json')
  request.add_header('Content-Length',str(len(urllib.urlencode(payload))))
  response = urllib2.urlopen(request).read()
  data = json.load(response)  
  if( data["deviceId"] != "0" ) 
    deviceId = data["deviceId"]
  message = data["message"]

# Main loop
loopCount = 0
while( loopCount < 10 ) and (deviceId = "")
  initialize()
  loopCount = loopCount + 1
  if(deviceId = "")
    print message
    sleep(0.1)


	

if(deviceId = "")
  print "Error during initialisation - quitting"
  quit()
  
  
  