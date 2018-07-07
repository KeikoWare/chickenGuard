import picamera
import base64
import io
import urllib
import urllib2

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
      cpuserial = "test323456789"
   return cpuserial

url = "https://www.keikoware.dk/info/capture/image.php"
camera = picamera.PiCamera()
camera.capture('image.jpg')

stream = io.BytesIO()
camera.capture(stream,'png')
stream.seek(0)
imgdata = base64.b64encode(stream.getvalue())
uid = getserial()
print uid
payload = {'filename':'gokkehuset.jpg','data':imgdata,'rpiSerial':uid} 
request = urllib2.Request(url,data=urllib.urlencode(payload))
request.add_header('Content-Type','application/x-www-form-urlencoded')
response = urllib2.urlopen(request).read()
print response
