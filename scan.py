#!/usr/bin/env python
"""scan.py: this runs a 360 degree scan"""

__author__      = "Robert Moser"
__copyright__ = "Copyright 2023  Robert Moser"
__credits__ = ["myslef for now"]
__license__ = "GPL"
__version__ = "0.0.0"
__maintainer__ = "Robert Moser"
__email__ = "whyamisoawkward2021@gmail.com"
__status__ = "prototype"

import subprocess
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib, GdkPixbuf
import serial
import datetime
from time import sleep
import time
import threading
import configparser
import os.path
import logging
import cv2
from subprocess import Popen
from ftplib import FTP
from GPSPhoto import gpsphoto
current_time = datetime.datetime.now()
from ftplib import FTP, error_perm

# Names varaible for configure parser
config = configparser.ConfigParser()

# Loading an ini that was created as a place holder for the current scans name.
# Just an easy way to pass information back and forth between the many process and subprocess the application needs to run.
config.read('settings.ini')

# This makes a varable for our current scan's name by parsing the information from slot created for it in our ini file 
filename = config['currentscaninfo']['currentscan']
# This makes varaibles from all the coordinates stored in settings
coordinatealongitude = config['coordinates']['coordinatealongitude']
coordinatealatitude = config['coordinates']['coordinatealatitude']
coordinateblongitude = config['coordinates']['coordinateblongitude']
coordinateblatitude = config['coordinates']['coordinateblatitude']
coordinateclongitude = config['coordinates']['coordinateclongitude']
coordinateclatitude = config['coordinates']['coordinateclatitude']
coordinatedlongitude = config['coordinates']['coordinatedlongitude']
coordinatedlatitude = config['coordinates']['coordinatedlatitude']
coordinateelongitude = config['coordinates']['coordinateelongitude']
coordinateelatitude = config['coordinates']['coordinateelatitude']
coordinateflongitude = config['coordinates']['coordinateflongitude']
coordinateflatitude = config['coordinates']['coordinateflatitude']
coordinateglongitude = config['coordinates']['coordinateglongitude']
coordinateglatitude = config['coordinates']['coordinateglatitude']
coordinatehlongitude = config['coordinates']['coordinatehlongitude']
coordinatehlatitude = config['coordinates']['coordinatehlatitude']
coordinateilongitude = config['coordinates']['coordinateilongitude']
coordinateilatitude = config['coordinates']['coordinateilatitude']
coordinatejlongitude = config['coordinates']['coordinatejlongitude']
coordinatejlatitude = config['coordinates']['coordinatejlatitude']
coordinateklongitude = config['coordinates']['coordinateklongitude']
coordinateklatitude = config['coordinates']['coordinateklatitude']
coordinatellongitude = config['coordinates']['coordinatellongitude']
coordinatellatitude = config['coordinates']['coordinatellatitude']
coordinatemlongitude = config['coordinates']['coordinatemlongitude']
coordinatemlatitude = config['coordinates']['coordinatemlatitude']
coordinatenlongitude = config['coordinates']['coordinatenlongitude']
coordinatenlatitude = config['coordinates']['coordinatenlatitude']
coordinateolongitude = config['coordinates']['coordinateolongitude']
coordinateolatitude = config['coordinates']['coordinateolatitude']
coordinateplongitude = config['coordinates']['coordinateplongitude']
coordinateplatitude = config['coordinates']['coordinateplatitude']
coordinateqlongitude = config['coordinates']['coordinateqlongitude']
coordinateqlatitude = config['coordinates']['coordinateqlatitude']
coordinaterlongitude = config['coordinates']['coordinaterlongitude']
coordinaterlatitude = config['coordinates']['coordinaterlatitude']
coordinateslongitude = config['coordinates']['coordinateslongitude']
coordinateslatitude = config['coordinates']['coordinateslatitude']
coordinatetlongitude = config['coordinates']['coordinatetlongitude']
coordinatetlatitude = config['coordinates']['coordinatetlatitude']
coordinateulongitude = config['coordinates']['coordinateulongitude']
coordinateulatitude = config['coordinates']['coordinateulatitude']
coordinatevlongitude = config['coordinates']['coordinatevlongitude']
coordinatevlatitude = config['coordinates']['coordinatevlatitude']
coordinatewlongitude = config['coordinates']['coordinatewlongitude']
coordinatewlatitude = config['coordinates']['coordinatewlatitude']
coordinatexlongitude = config['coordinates']['coordinatexlongitude']
coordinatexlatitude = config['coordinates']['coordinatexlatitude']

# This makes varaibles from all the server settings
serverip = config['serverinfo']['serveripaddress']
serveruser = config['serverinfo']['serverusername']
serverpassword = config['serverinfo']['serverpassword']
serverport = config['serverinfo']['serverportnumber']


# Needs to be in decimals so we float all this stuff and assign it a new name
coordinatealongitudefloated = float(coordinatealongitude)
coordinatealatitudefloated = float(coordinatealatitude)
coordinateblongitudefloated = float(coordinateblongitude)
coordinateblatitudefloated = float(coordinateblatitude)
coordinateclongitudefloated = float(coordinateclongitude)
coordinateclatitudefloated = float(coordinateclatitude)
coordinatedlongitudefloated = float(coordinatedlongitude)
coordinatedlatitudefloated = float(coordinatedlatitude)
coordinateelongitudefloated = float(coordinateelongitude)
coordinateelatitudefloated = float(coordinateelatitude)
coordinateflongitudefloated = float(coordinateflongitude)
coordinateflatitudefloated = float(coordinateflatitude)
coordinateglongitudefloated = float(coordinateglongitude)
coordinateglatitudefloated = float(coordinateglatitude)
coordinatehlongitudefloated = float(coordinatehlongitude)
coordinatehlatitudefloated = float(coordinatehlatitude)
coordinateilongitudefloated = float(coordinateilongitude)
coordinateilatitudefloated = float(coordinateilatitude)
coordinatejlongitudefloated = float(coordinatejlongitude)
coordinatejlatitudefloated = float(coordinatejlatitude)
coordinateklongitudefloated = float(coordinateklongitude)
coordinateklatitudefloated = float(coordinateklatitude)
coordinatellongitudefloated  = float(coordinatellongitude)
coordinatellatitudefloated = float(coordinatellatitude)
coordinatemlongitudefloated  = float(coordinatemlongitude)
coordinatemlatitudefloated = float(coordinatemlatitude)
coordinatenlongitudefloated = float(coordinatenlongitude)
coordinatenlatitudefloated = float(coordinatenlatitude)
coordinateolongitudefloated = float(coordinateolongitude)
coordinateolatitudefloated = float(coordinateolatitude)
coordinateplongitudefloated = float(coordinateplongitude)
coordinateplatitudefloated = float(coordinateplatitude)
coordinateqlongitudefloated  = float(coordinateqlongitude)
coordinateqlatitudefloated = float(coordinateqlatitude)
coordinaterlongitudefloated = float(coordinaterlongitude)
coordinaterlatitudefloated = float(coordinaterlatitude)
coordinateslongitudefloated = float(coordinateslongitude)
coordinateslatitudefloated = float(coordinateslatitude)
coordinatetlongitudefloated  = float(coordinatetlongitude)
coordinatetlatitudefloated = float(coordinatetlatitude)
coordinateulongitudefloated = float(coordinateulongitude)
coordinateulatitudefloated = float(coordinateulatitude)
coordinatevlongitudefloated = float(coordinatevlongitude)
coordinatevlatitudefloated = float(coordinatevlatitude)
coordinatewlongitudefloated = float(coordinatewlongitude)
coordinatewlatitudefloated = float(coordinatewlatitude)
coordinatexlongitudefloated = float(coordinatexlongitude)
coordinatexlatitudefloated = float(coordinatexlatitude)

# sets variable to plug in the users home directory
homedir = (os.path.expanduser('~'))

# making a variable to check to see if file exists aready before starting
path = (homedir + "/scans/" + filename +"/")
isExist = os.path.exists(path)

#setups the "info"
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('./logs/scan.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the file handler to the logger
logger.addHandler(handler)

# Connectiong to the Arduino. This is is alittle handler to connect to arduino 
# if for some reason it doesn't it will log it. 
try:
  
  logger.info("Attempting to connect to Arduino")
  platser = serial.Serial('/dev/ttyACM0', 115200)
except:
  print('Could not find arduino on assigned port')
  logger.warning('Could not find arduino on assigned port')
else:
  # Checking to see if the file we are about to create already exists
  # if the file does exist it launces a dialog box and program to allow the user option to
  #either over write or rename
  if isExist == True:
                print('Cannot scan file exists')
                logger.warning('Duplicate file name found loading handler')
                def callbackforduplicatescanname():
                    os.system("python3 dialogboxes/duplicatescanname.py")
                t = threading.Thread(target=callbackforduplicatescanname)
                t.start()

  else:
                print("Scan " + filename + " initiated utilizing a 24 image scan now")
                logger.info("Scan " + filename + " initiated utilizing a 24 image scan now")
                
                # This creates the directory to store file
                os.mkdir(homedir + "/scans/" +filename)

                # Taking picture with opencv
                videoCaptureObjectA = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret,frame = videoCaptureObjectA.read()
                    frame = cv2.rotate(frame, cv2.ROTATE_180)
                    cv2.imwrite(homedir + "/scans/" + filename +"/" + filename +"A.jpg",frame)
                    result = False
                videoCaptureObjectA.release()
                cv2.destroyAllWindows()
                logger.info(filename + "A.jpg captured located in: " + homedir + "/scans/" +filename)
                print(filename + "A.jpg captured located in: " + homedir + "/scans/" +filename)

                # Sends enough characters to turn the platform one quarter turn via the arduino hooked through serial connection
                platser.write('q1\n'.encode())
                
                print("motor rotated image taken")

                # Sleeps for 4 seconds to allows arduino time before we send it another command
                time.sleep(4)

                print("modifying GPS data for play well with")
                
                # Create a GPSPhoto Object to modify gps data to play well with Photogrammetry software
                photo = gpsphoto.GPSPhoto()
                photo = gpsphoto.GPSPhoto(homedir + "/scans/" + filename +"/" + filename +"A.jpg")

                # Create GPSInfo Data Object to modify gps data to play well with Photogrammetry software
                info = gpsphoto.GPSInfo((coordinatealongitudefloated, coordinatealatitudefloated))
                info = gpsphoto.GPSInfo((coordinatealongitudefloated, coordinatealatitudefloated), \
                  timeStamp=current_time)
                info = gpsphoto.GPSInfo((coordinatealongitudefloated, coordinatealatitudefloated), \
                  alt=10, timeStamp=current_time)

                # Modify GPS Data and resave image
                photo.modGPSData(info, homedir + "/scans/" + filename +"/" + filename +"A.jpg")

                print("/scans/" + filename +"/" + filename +"A.jpg")
                print('resaved with modified GPS Meta data')

                # Taking picture with opencv
                videoCaptureObjectB = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret,frame2 = videoCaptureObjectB.read()
                    frame2 = cv2.rotate(frame2, cv2.ROTATE_180)
                    cv2.imwrite(homedir + "/scans/" + filename +"/" + filename +"B.jpg",frame2)
                    result = False
                videoCaptureObjectB.release()
                cv2.destroyAllWindows()
                logger.info(filename + "B.jpg captured located in: " + homedir + "/scans/" +filename)
                print(filename + "B.jpg captured located in: " + homedir + "/scans/" +filename)

                # Sends enough characters to turn the platform one quarter turn via the arduino hooked through serial connection
                platser.write('q1\n'.encode())
                
                print("motor rotated image taken")

                print("modifying GPS data for play well with")
                # Create a GPSPhoto Object to modify gps data to play well with Photogrammetry software
                photo = gpsphoto.GPSPhoto()
                photo = gpsphoto.GPSPhoto(homedir + "/scans/" + filename +"/" + filename +"B.jpg")

                # Create GPSInfo Data Object to modify gps data to play well with Photogrammetry software
                info = gpsphoto.GPSInfo((coordinateblongitudefloated, coordinateblatitudefloated))
                info = gpsphoto.GPSInfo((coordinateblongitudefloated, coordinateblatitudefloated), \
                  timeStamp=current_time)
                info = gpsphoto.GPSInfo((coordinateblongitudefloated, coordinateblatitudefloated), \
                  alt=10, timeStamp=current_time)

                # Modify GPS Data and resave image
                photo.modGPSData(info, homedir + "/scans/" + filename +"/" + filename +"B.jpg")

                print("/scans/" + filename +"/" + filename +"B.jpg")
                print('resaved with modified GPS Meta data')

                #sleep for 4 seconds allows arduino time before we send it another command
                time.sleep(4)

              # Taking picture with opencv
                videoCaptureObjectC = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret,frame3 = videoCaptureObjectC.read()
                    frame3 = cv2.rotate(frame3, cv2.ROTATE_180)
                    cv2.imwrite(homedir + "/scans/" + filename +"/" + filename +"C.jpg",frame3)
                    result = False
                videoCaptureObjectC.release()
                cv2.destroyAllWindows()
                logger.info(filename + "C.jpg captured located in: " + homedir + "/scans/" +filename)
                print(filename + "C.jpg captured located in: " + homedir + "/scans/" +filename)

                # Sends enough characters to turn the platform one quarter turn via the arduino hooked through serial connection
                platser.write('q1\n'.encode())
                
                print("motor rotated image taken")

                #sleep for 4 seconds allows arduino time before we send it another command
                time.sleep(4)

                print("modifying GPS data for play well with")
                # Create a GPSPhoto Object to modify gps data to play well with Photogrammetry software
                photo = gpsphoto.GPSPhoto()
                photo = gpsphoto.GPSPhoto(homedir + "/scans/" + filename +"/" + filename +"C.jpg")

                # Create GPSInfo Data Object to modify gps data to play well with Photogrammetry software
                info = gpsphoto.GPSInfo((coordinateclongitudefloated, coordinateclatitudefloated))
                info = gpsphoto.GPSInfo((coordinateclongitudefloated, coordinateclatitudefloated), \
                  timeStamp=current_time)
                info = gpsphoto.GPSInfo((coordinateclongitudefloated, coordinateclatitudefloated), \
                  alt=10, timeStamp=current_time)

                # Modify GPS Data and resave image
                photo.modGPSData(info, homedir + "/scans/" + filename +"/" + filename +"C.jpg")

                print("/scans/" + filename +"/" + filename +"C.jpg")
                print('resaved with modified GPS Meta data')

                # Taking picture with opencv
                videoCaptureObjectD = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret,frame4 = videoCaptureObjectD.read()
                    frame4 = cv2.rotate(frame4, cv2.ROTATE_180)
                    cv2.imwrite(homedir + "/scans/" + filename +"/" + filename +"D.jpg",frame4)
                    result = False
                videoCaptureObjectD.release()
                cv2.destroyAllWindows()
                logger.info(filename + "D.jpg captured located in: " + homedir + "/scans/" +filename)
                print(filename + "D.jpg captured located in: " + homedir + "/scans/" +filename)

                # Sends enough characters to turn the platform one quarter turn via the arduino hooked through serial connection
                platser.write('q1\n'.encode())
                
                print("motor rotated image taken")

                #sleep for 4 seconds allows arduino time before we send it another command
                time.sleep(4)

                print("modifying GPS data for play well with")
                # Create a GPSPhoto Object to modify gps data to play well with Photogrammetry software
                photo = gpsphoto.GPSPhoto()
                photo = gpsphoto.GPSPhoto(homedir + "/scans/" + filename +"/" + filename +"D.jpg")

                # Create GPSInfo Data Object to modify gps data to play well with Photogrammetry software
                info = gpsphoto.GPSInfo((coordinatedlongitudefloated, coordinatedlatitudefloated))
                info = gpsphoto.GPSInfo((coordinatedlongitudefloated, coordinatedlatitudefloated), \
                  timeStamp=current_time)
                info = gpsphoto.GPSInfo((coordinatedlongitudefloated, coordinatedlatitudefloated), \
                  alt=10, timeStamp=current_time)

                # Modify GPS Data and resave image
                photo.modGPSData(info, homedir + "/scans/" + filename +"/" + filename +"D.jpg")

                print("/scans/" + filename +"/" + filename +"D.jpg")
                print('resaved with modified GPS Meta data')

                # Taking picture with opencv
                videoCaptureObjectE = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret,frame5 = videoCaptureObjectE.read()
                    frame5 = cv2.rotate(frame5, cv2.ROTATE_180)
                    cv2.imwrite(homedir + "/scans/" + filename +"/" + filename +"E.jpg",frame5)
                    result = False
                videoCaptureObjectE.release()
                cv2.destroyAllWindows()
                logger.info(filename + "E.jpg captured located in: " + homedir + "/scans/" +filename)
                print(filename + "E.jpg captured located in: " + homedir + "/scans/" +filename)

                # Sends enough characters to turn the platform one quarter turn via the arduino hooked through serial connection
                platser.write('q1\n'.encode())
                
                print("motor rotated image taken")

                #sleep for 4 seconds allows arduino time before we send it another command
                time.sleep(4)

                print("modifying GPS data for play well with")
                # Create a GPSPhoto Object to modify gps data to play well with Photogrammetry software
                photo = gpsphoto.GPSPhoto()
                photo = gpsphoto.GPSPhoto(homedir + "/scans/" + filename +"/" + filename +"E.jpg")

                # Create GPSInfo Data Object to modify gps data to play well with Photogrammetry software
                info = gpsphoto.GPSInfo((coordinateelongitudefloated, coordinateelatitudefloated))
                info = gpsphoto.GPSInfo((coordinateelongitudefloated, coordinateelatitudefloated), \
                  timeStamp=current_time)
                info = gpsphoto.GPSInfo((coordinateelongitudefloated, coordinateelatitudefloated), \
                  alt=10, timeStamp=current_time)

                # Modify GPS Data and resave image
                photo.modGPSData(info, homedir + "/scans/" + filename +"/" + filename +"E.jpg")

                print("/scans/" + filename +"/" + filename +"E.jpg")
                print('resaved with modified GPS Meta data')

              # Taking picture with opencv
                videoCaptureObjectF = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret,frame6 = videoCaptureObjectF.read()
                    frame6 = cv2.rotate(frame6, cv2.ROTATE_180)
                    cv2.imwrite(homedir + "/scans/" + filename +"/" + filename +"F.jpg",frame6)
                    result = False
                videoCaptureObjectF.release()
                cv2.destroyAllWindows()
                logger.info(filename + "F.jpg captured located in: " + homedir + "/scans/" +filename)
                print(filename + "F.jpg captured located in: " + homedir + "/scans/" +filename)

                # Sends enough characters to turn the platform one quarter turn via the arduino hooked through serial connection
                platser.write('q1\n'.encode())
                
                print("motor rotated image taken")

                #sleep for 4 seconds allows arduino time before we send it another command
                time.sleep(4)

                print("modifying GPS data for play well with")
                # Create a GPSPhoto Object to modify gps data to play well with Photogrammetry software
                photo = gpsphoto.GPSPhoto()
                photo = gpsphoto.GPSPhoto(homedir + "/scans/" + filename +"/" + filename +"F.jpg")

                # Create GPSInfo Data Object to modify gps data to play well with Photogrammetry software
                info = gpsphoto.GPSInfo((coordinateflongitudefloated, coordinateflatitudefloated))
                info = gpsphoto.GPSInfo((coordinateflongitudefloated, coordinateflatitudefloated), \
                  timeStamp=current_time)
                info = gpsphoto.GPSInfo((coordinateflongitudefloated, coordinateflatitudefloated), \
                  alt=10, timeStamp=current_time)

                # Modify GPS Data and resave image
                photo.modGPSData(info, homedir + "/scans/" + filename +"/" + filename +"F.jpg")

                print("/scans/" + filename +"/" + filename +"F.jpg")
                print('resaved with modified GPS Meta data')

                # Taking picture with opencv
                videoCaptureObjectG = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret,frame7 = videoCaptureObjectG.read()
                    frame7 = cv2.rotate(frame7, cv2.ROTATE_180)
                    cv2.imwrite(homedir + "/scans/" + filename +"/" + filename +"G.jpg",frame7)
                    result = False
                videoCaptureObjectG.release()
                cv2.destroyAllWindows()
                logger.info(filename + "G.jpg captured located in: " + homedir + "/scans/" +filename)
                print(filename + "G.jpg captured located in: " + homedir + "/scans/" +filename)

                # Sends enough characters to turn the platform one quarter turn via the arduino hooked through serial connection
                platser.write('q1\n'.encode())
                
                print("motor rotated image taken")

                #sleep for 4 seconds allows arduino time before we send it another command
                time.sleep(4)

                print("modifying GPS data for play well with")
                # Create a GPSPhoto Object to modify gps data to play well with Photogrammetry software
                photo = gpsphoto.GPSPhoto()
                photo = gpsphoto.GPSPhoto(homedir + "/scans/" + filename +"/" + filename +"G.jpg")

                # Create GPSInfo Data Object to modify gps data to play well with Photogrammetry software
                info = gpsphoto.GPSInfo((coordinateglongitudefloated, coordinateglatitudefloated))
                info = gpsphoto.GPSInfo((coordinateglongitudefloated, coordinateglatitudefloated), \
                  timeStamp=current_time)
                info = gpsphoto.GPSInfo((coordinateglongitudefloated, coordinateglatitudefloated), \
                  alt=10, timeStamp=current_time)

                # Modify GPS Data and resave image
                photo.modGPSData(info, homedir + "/scans/" + filename +"/" + filename +"G.jpg")

                print("/scans/" + filename +"/" + filename +"G.jpg")
                print('resaved with modified GPS Meta data')

                # Taking picture with opencv
                videoCaptureObjectH = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret,frame8 = videoCaptureObjectH.read()
                    frame8 = cv2.rotate(frame8, cv2.ROTATE_180)
                    cv2.imwrite(homedir + "/scans/" + filename +"/" + filename +"H.jpg",frame8)
                    result = False
                videoCaptureObjectH.release()
                cv2.destroyAllWindows()
                logger.info(filename + "H.jpg captured located in: " + homedir + "/scans/" +filename)
                print(filename + "H.jpg captured located in: " + homedir + "/scans/" +filename)

                # Sends enough characters to turn the platform one quarter turn via the arduino hooked through serial connection
                platser.write('q1\n'.encode())
                
                print("motor rotated image taken")

                #sleep for 4 seconds allows arduino time before we send it another command
                time.sleep(4)

                print("modifying GPS data for play well with")
                # Create a GPSPhoto Object to modify gps data to play well with Photogrammetry software
                photo = gpsphoto.GPSPhoto()
                photo = gpsphoto.GPSPhoto(homedir + "/scans/" + filename +"/" + filename +"H.jpg")

                # Create GPSInfo Data Object to modify gps data to play well with Photogrammetry software
                info = gpsphoto.GPSInfo((coordinatehlongitudefloated, coordinatehlatitudefloated))
                info = gpsphoto.GPSInfo((coordinatehlongitudefloated, coordinatehlatitudefloated), \
                  timeStamp=current_time)
                info = gpsphoto.GPSInfo((coordinatehlongitudefloated, coordinatehlatitudefloated), \
                  alt=10, timeStamp=current_time)

                # Modify GPS Data and resave image
                photo.modGPSData(info, homedir + "/scans/" + filename +"/" + filename +"H.jpg")

                print("/scans/" + filename +"/" + filename +"H.jpg")
                print('resaved with modified GPS Meta data')

                ## Taking picture with opencv
                videoCaptureObjectI = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret,frame9 = videoCaptureObjectI.read()
                    frame9 = cv2.rotate(frame9, cv2.ROTATE_180)
                    cv2.imwrite(homedir + "/scans/" + filename +"/" + filename +"I.jpg",frame9)
                    result = False
                videoCaptureObjectI.release()
                cv2.destroyAllWindows()
                logger.info(filename + "I.jpg captured located in: " + homedir + "/scans/" +filename)
                print(filename + "I.jpg captured located in: " + homedir + "/scans/" +filename)

                # Sends enough characters to turn the platform one quarter turn via the arduino hooked through serial connection
                platser.write('q1\n'.encode())
                
                print("motor rotated image taken")

                #sleep for 4 seconds allows arduino time before we send it another command
                time.sleep(4)

                print("modifying GPS data for play well with")
                # Create a GPSPhoto Object to modify gps data to play well with Photogrammetry software
                photo = gpsphoto.GPSPhoto()
                photo = gpsphoto.GPSPhoto(homedir + "/scans/" + filename +"/" + filename +"I.jpg")

                # Create GPSInfo Data Object to modify gps data to play well with Photogrammetry software
                info = gpsphoto.GPSInfo((coordinateilongitudefloated, coordinateilatitudefloated))
                info = gpsphoto.GPSInfo((coordinateilongitudefloated, coordinateilatitudefloated), \
                  timeStamp=current_time)
                info = gpsphoto.GPSInfo((coordinateilongitudefloated, coordinateilatitudefloated), \
                  alt=10, timeStamp=current_time)

                # Modify GPS Data and resave image
                photo.modGPSData(info, homedir + "/scans/" + filename +"/" + filename +"I.jpg")

                print("/scans/" + filename +"/" + filename +"I.jpg")
                print('resaved with modified GPS Meta data')

                # Taking picture with opencv
                videoCaptureObjectJ = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret,frame10 = videoCaptureObjectJ.read()
                    frame10 = cv2.rotate(frame10, cv2.ROTATE_180)
                    cv2.imwrite(homedir + "/scans/" + filename +"/" + filename +"J.jpg",frame10)
                    result = False
                videoCaptureObjectJ.release()
                cv2.destroyAllWindows()
                logger.info(filename + "J.jpg captured located in: " + homedir + "/scans/" +filename)
                print(filename + "J.jpg captured located in: " + homedir + "/scans/" +filename)

                # Sends enough characters to turn the platform one quarter turn via the arduino hooked through serial connection
                platser.write('q1\n'.encode())
                
                print("motor rotated image taken")

                #sleep for 4 seconds allows arduino time before we send it another command
                time.sleep(4)

                print("modifying GPS data for play well with")
                # Create a GPSPhoto Object to modify gps data to play well with Photogrammetry software
                photo = gpsphoto.GPSPhoto()
                photo = gpsphoto.GPSPhoto(homedir + "/scans/" + filename +"/" + filename +"J.jpg")

                # Create GPSInfo Data Object to modify gps data to play well with Photogrammetry software
                info = gpsphoto.GPSInfo((coordinatejlongitudefloated, coordinatejlatitudefloated))
                info = gpsphoto.GPSInfo((coordinatejlongitudefloated, coordinatejlatitudefloated), \
                  timeStamp=current_time)
                info = gpsphoto.GPSInfo((coordinatejlongitudefloated, coordinatejlatitudefloated), \
                  alt=10, timeStamp=current_time)

                # Modify GPS Data and resave image
                photo.modGPSData(info, homedir + "/scans/" + filename +"/" + filename +"J.jpg")

                print("/scans/" + filename +"/" + filename +"J.jpg")
                print('resaved with modified GPS Meta data')

                # Taking picture with opencv
                videoCaptureObjectK = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret,frame11 = videoCaptureObjectK.read()
                    frame11 = cv2.rotate(frame11, cv2.ROTATE_180)
                    cv2.imwrite(homedir + "/scans/" + filename +"/" + filename +"K.jpg",frame11)
                    result = False
                videoCaptureObjectK.release()
                cv2.destroyAllWindows()
                logger.info(filename + "K.jpg captured located in: " + homedir + "/scans/" +filename)
                print(filename + "K.jpg captured located in: " + homedir + "/scans/" +filename)

                # Sends enough characters to turn the platform one quarter turn via the arduino hooked through serial connection
                platser.write('q1\n'.encode())
                
                print("motor rotated image taken")

                #sleep for 4 seconds allows arduino time before we send it another command
                time.sleep(4)

                print("modifying GPS data for play well with")
                # Create a GPSPhoto Object to modify gps data to play well with Photogrammetry software
                photo = gpsphoto.GPSPhoto()
                photo = gpsphoto.GPSPhoto(homedir + "/scans/" + filename +"/" + filename +"K.jpg")

                # Create GPSInfo Data Object to modify gps data to play well with Photogrammetry software
                info = gpsphoto.GPSInfo((coordinateklongitudefloated, coordinateklatitudefloated))
                info = gpsphoto.GPSInfo((coordinateklongitudefloated, coordinateklatitudefloated), \
                  timeStamp=current_time)
                info = gpsphoto.GPSInfo((coordinateklongitudefloated, coordinateklatitudefloated), \
                  alt=10, timeStamp=current_time)

                # Modify GPS Data and resave image
                photo.modGPSData(info, homedir + "/scans/" + filename +"/" + filename +"K.jpg")

                print("/scans/" + filename +"/" + filename +"K.jpg")
                print('resaved with modified GPS Meta data')

                # Taking picture with opencv
                videoCaptureObjectL = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret,frame12 = videoCaptureObjectL.read()
                    frame12 = cv2.rotate(frame12, cv2.ROTATE_180)
                    cv2.imwrite(homedir + "/scans/" + filename +"/" + filename +"L.jpg",frame12)
                    result = False
                videoCaptureObjectL.release()
                cv2.destroyAllWindows()
                logger.info(filename + "L.jpg captured located in: " + homedir + "/scans/" +filename)
                print(filename + "L.jpg captured located in: " + homedir + "/scans/" +filename)

                # Sends enough characters to turn the platform one quarter turn via the arduino hooked through serial connection
                platser.write('q1\n'.encode())
                
                print("motor rotated image taken")

                #sleep for 4 seconds allows arduino time before we send it another command
                time.sleep(4)

                print("modifying GPS data for play well with")
                # Create a GPSPhoto Object to modify gps data to play well with Photogrammetry software
                photo = gpsphoto.GPSPhoto()
                photo = gpsphoto.GPSPhoto(homedir + "/scans/" + filename +"/" + filename +"L.jpg")

                # Create GPSInfo Data Object to modify gps data to play well with Photogrammetry software
                info = gpsphoto.GPSInfo((coordinatellongitudefloated, coordinatellatitudefloated))
                info = gpsphoto.GPSInfo((coordinatellongitudefloated, coordinatellatitudefloated), \
                  timeStamp=current_time)
                info = gpsphoto.GPSInfo((coordinatellongitudefloated, coordinatellatitudefloated), \
                  alt=10, timeStamp=current_time)

                # Modify GPS Data and resave image
                photo.modGPSData(info, homedir + "/scans/" + filename +"/" + filename +"L.jpg")

                print("/scans/" + filename +"/" + filename +"L.jpg")
                print('resaved with modified GPS Meta data')

                # Taking picture with opencv
                videoCaptureObjectM = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret,frame13 = videoCaptureObjectM.read()
                    frame13 = cv2.rotate(frame13, cv2.ROTATE_180)
                    cv2.imwrite(homedir + "/scans/" + filename +"/" + filename +"M.jpg",frame13)
                    result = False
                videoCaptureObjectM.release()
                cv2.destroyAllWindows()
                logger.info(filename + "M.jpg captured located in: " + homedir + "/scans/" +filename)
                print(filename + "M.jpg captured located in: " + homedir + "/scans/" +filename)

                # Sends enough characters to turn the platform one quarter turn via the arduino hooked through serial connection
                platser.write('q1\n'.encode())
                
                print("motor rotated image taken")

                #sleep for 4 seconds allows arduino time before we send it another command
                time.sleep(4)

                print("modifying GPS data for play well with")
                # Create a GPSPhoto Object to modify gps data to play well with Photogrammetry software
                photo = gpsphoto.GPSPhoto()
                photo = gpsphoto.GPSPhoto(homedir + "/scans/" + filename +"/" + filename +"M.jpg")

                # Create GPSInfo Data Object to modify gps data to play well with Photogrammetry software
                info = gpsphoto.GPSInfo((coordinatemlongitudefloated, coordinatemlatitudefloated))
                info = gpsphoto.GPSInfo((coordinatemlongitudefloated, coordinatemlatitudefloated), \
                  timeStamp=current_time)
                info = gpsphoto.GPSInfo((coordinatemlongitudefloated, coordinatemlatitudefloated), \
                  alt=10, timeStamp=current_time)

                # Modify GPS Data and resave image
                photo.modGPSData(info, homedir + "/scans/" + filename +"/" + filename +"M.jpg")

                print("/scans/" + filename +"/" + filename +"M.jpg")
                print('resaved with modified GPS Meta data')

                # Taking picture with opencv
                videoCaptureObjectN = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret,frame14 = videoCaptureObjectN.read()
                    frame14 = cv2.rotate(frame14, cv2.ROTATE_180)
                    cv2.imwrite(homedir + "/scans/" + filename +"/" + filename +"N.jpg",frame14)
                    result = False
                videoCaptureObjectN.release()
                cv2.destroyAllWindows()
                logger.info(filename + "N.jpg captured located in: " + homedir + "/scans/" +filename)
                print(filename + "N.jpg captured located in: " + homedir + "/scans/" +filename)

                # Sends enough characters to turn the platform one quarter turn via the arduino hooked through serial connection
                platser.write('q1\n'.encode())
                
                print("motor rotated image taken")

                #sleep for 4 seconds allows arduino time before we send it another command
                time.sleep(4)

                print("modifying GPS data for play well with")
                # Create a GPSPhoto Object to modify gps data to play well with Photogrammetry software
                photo = gpsphoto.GPSPhoto()
                photo = gpsphoto.GPSPhoto(homedir + "/scans/" + filename +"/" + filename +"N.jpg")

                # Create GPSInfo Data Object to modify gps data to play well with Photogrammetry software
                info = gpsphoto.GPSInfo((coordinatenlongitudefloated, coordinatenlatitudefloated))
                info = gpsphoto.GPSInfo((coordinatenlongitudefloated, coordinatenlatitudefloated), \
                  timeStamp=current_time)
                info = gpsphoto.GPSInfo((coordinatenlongitudefloated, coordinatenlatitudefloated), \
                  alt=10, timeStamp=current_time)

                # Modify GPS Data and resave image
                photo.modGPSData(info, homedir + "/scans/" + filename +"/" + filename +"N.jpg")

                print("/scans/" + filename +"/" + filename +"N.jpg")
                print('resaved with modified GPS Meta data')

                # Taking picture with opencv
                videoCaptureObjectO = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret,frame15 = videoCaptureObjectO.read()
                    frame15 = cv2.rotate(frame15, cv2.ROTATE_180)
                    cv2.imwrite(homedir + "/scans/" + filename +"/" + filename +"O.jpg",frame15)
                    result = False
                videoCaptureObjectO.release()
                cv2.destroyAllWindows()
                logger.info(filename + "O.jpg captured located in: " + homedir + "/scans/" +filename)
                print(filename + "O.jpg captured located in: " + homedir + "/scans/" +filename)

                # Sends enough characters to turn the platform one quarter turn via the arduino hooked through serial connection
                platser.write('q1\n'.encode())
                
                print("motor rotated image taken")

                #sleep for 4 seconds allows arduino time before we send it another command
                time.sleep(4)

                print("modifying GPS data for play well with")
                # Create a GPSPhoto Object to modify gps data to play well with Photogrammetry software
                photo = gpsphoto.GPSPhoto()
                photo = gpsphoto.GPSPhoto(homedir + "/scans/" + filename +"/" + filename +"O.jpg")

                # Create GPSInfo Data Object to modify gps data to play well with Photogrammetry software
                info = gpsphoto.GPSInfo((coordinateolongitudefloated, coordinateolatitudefloated))
                info = gpsphoto.GPSInfo((coordinateolongitudefloated, coordinateolatitudefloated), \
                  timeStamp=current_time)
                info = gpsphoto.GPSInfo((coordinateolongitudefloated, coordinateolatitudefloated), \
                  alt=10, timeStamp=current_time)

                # Modify GPS Data and resave image
                photo.modGPSData(info, homedir + "/scans/" + filename +"/" + filename +"O.jpg")

                print("/scans/" + filename +"/" + filename +"O.jpg")
                print('resaved with modified GPS Meta data')

                # Taking picture with opencv
                videoCaptureObjectP = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret,frame16 = videoCaptureObjectP.read()
                    frame16 = cv2.rotate(frame16, cv2.ROTATE_180)
                    cv2.imwrite(homedir + "/scans/" + filename +"/" + filename +"P.jpg",frame16)
                    result = False
                videoCaptureObjectP.release()
                cv2.destroyAllWindows()
                logger.info(filename + "P.jpg captured located in: " + homedir + "/scans/" +filename)
                print(filename + "P.jpg captured located in: " + homedir + "/scans/" +filename)

                # Sends enough characters to turn the platform one quarter turn via the arduino hooked through serial connection
                platser.write('q1\n'.encode())
                
                print("motor rotated image taken")

                #sleep for 4 seconds allows arduino time before we send it another command
                time.sleep(4)

                print("modifying GPS data for play well with")
                # Create a GPSPhoto Object to modify gps data to play well with Photogrammetry software
                photo = gpsphoto.GPSPhoto()
                photo = gpsphoto.GPSPhoto(homedir + "/scans/" + filename +"/" + filename +"P.jpg")

                # Create GPSInfo Data Object to modify gps data to play well with Photogrammetry software
                info = gpsphoto.GPSInfo((coordinateplongitudefloated, coordinateplatitudefloated))
                info = gpsphoto.GPSInfo((coordinateplongitudefloated, coordinateplatitudefloated), \
                  timeStamp=current_time)
                info = gpsphoto.GPSInfo((coordinateplongitudefloated, coordinateplatitudefloated), \
                  alt=10, timeStamp=current_time)

                # Modify GPS Data and resave image
                photo.modGPSData(info, homedir + "/scans/" + filename +"/" + filename +"P.jpg")

                print("/scans/" + filename +"/" + filename +"P.jpg")
                print('resaved with modified GPS Meta data')

                # Taking picture with opencv
                videoCaptureObjectQ = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret,frame17 = videoCaptureObjectQ.read()
                    frame17 = cv2.rotate(frame17, cv2.ROTATE_180)
                    cv2.imwrite(homedir + "/scans/" + filename +"/" + filename +"Q.jpg",frame17)
                    result = False
                videoCaptureObjectQ.release()
                cv2.destroyAllWindows()
                logger.info(filename + "Q.jpg captured located in: " + homedir + "/scans/" +filename)
                print(filename + "Q.jpg captured located in: " + homedir + "/scans/" +filename)

                # Sends enough characters to turn the platform one quarter turn via the arduino hooked through serial connection
                platser.write('q1\n'.encode())
                
                print("motor rotated image taken")

                #sleep for 4 seconds allows arduino time before we send it another command
                time.sleep(4)

                print("modifying GPS data for play well with")
                # Create a GPSPhoto Object to modify gps data to play well with Photogrammetry software
                photo = gpsphoto.GPSPhoto()
                photo = gpsphoto.GPSPhoto(homedir + "/scans/" + filename +"/" + filename +"Q.jpg")

                # Create GPSInfo Data Object to modify gps data to play well with Photogrammetry software
                info = gpsphoto.GPSInfo((coordinateqlongitudefloated, coordinateqlatitudefloated))
                info = gpsphoto.GPSInfo((coordinateqlongitudefloated, coordinateqlatitudefloated), \
                  timeStamp=current_time)
                info = gpsphoto.GPSInfo((coordinateqlongitudefloated, coordinateqlatitudefloated), \
                  alt=10, timeStamp=current_time)

                # Modify GPS Data and resave image
                photo.modGPSData(info, homedir + "/scans/" + filename +"/" + filename +"Q.jpg")

                print("/scans/" + filename +"/" + filename +"Q.jpg")
                print('resaved with modified GPS Meta data')

                # Taking picture with opencv
                videoCaptureObjectR = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret,frame18 = videoCaptureObjectR.read()
                    frame18 = cv2.rotate(frame18, cv2.ROTATE_180)
                    cv2.imwrite(homedir + "/scans/" + filename +"/" + filename +"R.jpg",frame18)
                    result = False
                videoCaptureObjectR.release()
                cv2.destroyAllWindows()
                logger.info(filename + "R.jpg captured located in: " + homedir + "/scans/" +filename)
                print(filename + "R.jpg captured located in: " + homedir + "/scans/" +filename)

                # Sends enough characters to turn the platform one quarter turn via the arduino hooked through serial connection
                platser.write('q1\n'.encode())
                
                print("motor rotated image taken")

                #sleep for 4 seconds allows arduino time before we send it another command
                time.sleep(4)

                print("modifying GPS data for play well with")
                # Create a GPSPhoto Object to modify gps data to play well with Photogrammetry software
                photo = gpsphoto.GPSPhoto()
                photo = gpsphoto.GPSPhoto(homedir + "/scans/" + filename +"/" + filename +"R.jpg")

                # Create GPSInfo Data Object to modify gps data to play well with Photogrammetry software
                info = gpsphoto.GPSInfo((coordinaterlongitudefloated, coordinaterlatitudefloated))
                info = gpsphoto.GPSInfo((coordinaterlongitudefloated, coordinaterlatitudefloated), \
                  timeStamp=current_time)
                info = gpsphoto.GPSInfo((coordinaterlongitudefloated, coordinaterlatitudefloated), \
                  alt=10, timeStamp=current_time)

                # Modify GPS Data and resave image
                photo.modGPSData(info, homedir + "/scans/" + filename +"/" + filename +"R.jpg")

                print("/scans/" + filename +"/" + filename +"R.jpg")
                print('resaved with modified GPS Meta data')

                # Taking picture with opencv
                videoCaptureObjectS = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret,frame19 = videoCaptureObjectS.read()
                    frame19 = cv2.rotate(frame19, cv2.ROTATE_180)
                    cv2.imwrite(homedir + "/scans/" + filename +"/" + filename +"S.jpg",frame19)
                    result = False
                videoCaptureObjectS.release()
                cv2.destroyAllWindows()
                logger.info(filename + "S.jpg captured located in: " + homedir + "/scans/" +filename)
                print(filename + "S.jpg captured located in: " + homedir + "/scans/" +filename)

                # Sends enough characters to turn the platform one quarter turn via the arduino hooked through serial connection
                platser.write('q1\n'.encode())
                
                print("motor rotated image taken")

                #sleep for 4 seconds allows arduino time before we send it another command
                time.sleep(4)

                print("modifying GPS data for play well with")
                # Create a GPSPhoto Object to modify gps data to play well with Photogrammetry software
                photo = gpsphoto.GPSPhoto()
                photo = gpsphoto.GPSPhoto(homedir + "/scans/" + filename +"/" + filename +"S.jpg")

                # Create GPSInfo Data Object to modify gps data to play well with Photogrammetry software
                info = gpsphoto.GPSInfo((coordinateslongitudefloated, coordinateslatitudefloated))
                info = gpsphoto.GPSInfo((coordinateslongitudefloated, coordinateslatitudefloated), \
                  timeStamp=current_time)
                info = gpsphoto.GPSInfo((coordinateslongitudefloated, coordinateslatitudefloated), \
                  alt=10, timeStamp=current_time)

                # Modify GPS Data and resave image
                photo.modGPSData(info, homedir + "/scans/" + filename +"/" + filename +"S.jpg")

                print("/scans/" + filename +"/" + filename +"S.jpg")
                print('resaved with modified GPS Meta data')

                # Taking picture with opencv
                videoCaptureObjectT = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret,frame20 = videoCaptureObjectT.read()
                    frame20 = cv2.rotate(frame20, cv2.ROTATE_180)
                    cv2.imwrite(homedir + "/scans/" + filename +"/" + filename +"T.jpg",frame20)
                    result = False
                videoCaptureObjectT.release()
                cv2.destroyAllWindows()
                logger.info(filename + "T.jpg captured located in: " + homedir + "/scans/" +filename)
                print(filename + "T.jpg captured located in: " + homedir + "/scans/" +filename)

                # Sends enough characters to turn the platform one quarter turn via the arduino hooked through serial connection
                platser.write('q1\n'.encode())
                
                print("motor rotated image taken")

                #sleep for 4 seconds allows arduino time before we send it another command
                time.sleep(4)

                print("modifying GPS data for play well with")
                # Create a GPSPhoto Object to modify gps data to play well with Photogrammetry software
                photo = gpsphoto.GPSPhoto()
                photo = gpsphoto.GPSPhoto(homedir + "/scans/" + filename +"/" + filename +"T.jpg")

                # Create GPSInfo Data Object to modify gps data to play well with Photogrammetry software
                info = gpsphoto.GPSInfo((coordinatetlongitudefloated, coordinatetlatitudefloated))
                info = gpsphoto.GPSInfo((coordinatetlongitudefloated, coordinatetlatitudefloated), \
                  timeStamp=current_time)
                info = gpsphoto.GPSInfo((coordinatetlongitudefloated, coordinatetlatitudefloated), \
                  alt=10, timeStamp=current_time)

                # Modify GPS Data and resave image
                photo.modGPSData(info, homedir + "/scans/" + filename +"/" + filename +"T.jpg")

                print("/scans/" + filename +"/" + filename +"T.jpg")
                print('resaved with modified GPS Meta data')

                # Taking picture with opencv
                videoCaptureObjectU = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret,frame21 = videoCaptureObjectU.read()
                    frame21 = cv2.rotate(frame21, cv2.ROTATE_180)
                    cv2.imwrite(homedir + "/scans/" + filename +"/" + filename +"U.jpg",frame21)
                    result = False
                videoCaptureObjectU.release()
                cv2.destroyAllWindows()
                logger.info(filename + "U.jpg captured located in: " + homedir + "/scans/" +filename)
                print(filename + "U.jpg captured located in: " + homedir + "/scans/" +filename)

                # Sends enough characters to turn the platform one quarter turn via the arduino hooked through serial connection
                platser.write('q1\n'.encode())
                
                print("motor rotated image taken")

                #sleep for 4 seconds allows arduino time before we send it another command
                time.sleep(4)

                print("modifying GPS data for play well with")
                # Create a GPSPhoto Object to modify gps data to play well with Photogrammetry software
                photo = gpsphoto.GPSPhoto()
                photo = gpsphoto.GPSPhoto(homedir + "/scans/" + filename +"/" + filename +"U.jpg")

                # Create GPSInfo Data Object to modify gps data to play well with Photogrammetry software
                info = gpsphoto.GPSInfo((coordinateulongitudefloated, coordinateulatitudefloated))
                info = gpsphoto.GPSInfo((coordinateulongitudefloated, coordinateulatitudefloated), \
                  timeStamp=current_time)
                info = gpsphoto.GPSInfo((coordinateulongitudefloated, coordinateulatitudefloated), \
                  alt=10, timeStamp=current_time)

                # Modify GPS Data and resave image
                photo.modGPSData(info, homedir + "/scans/" + filename +"/" + filename +"U.jpg")

                print("/scans/" + filename +"/" + filename +"U.jpg")
                print('resaved with modified GPS Meta data')

                # Taking picture with opencv
                videoCaptureObjectV = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret,frame22 = videoCaptureObjectV.read()
                    frame22 = cv2.rotate(frame22, cv2.ROTATE_180)
                    cv2.imwrite(homedir + "/scans/" + filename +"/" + filename +"V.jpg",frame22)
                    result = False
                videoCaptureObjectV.release()
                cv2.destroyAllWindows()
                logger.info(filename + "V.jpg captured located in: " + homedir + "/scans/" +filename)
                print(filename + "V.jpg captured located in: " + homedir + "/scans/" +filename)

                # Sends enough characters to turn the platform one quarter turn via the arduino hooked through serial connection
                platser.write('q1\n'.encode())
                
                print("motor rotated image taken")

                #sleep for 4 seconds allows arduino time before we send it another command
                time.sleep(4)

                print("modifying GPS data for play well with")
                # Create a GPSPhoto Object to modify gps data to play well with Photogrammetry software
                photo = gpsphoto.GPSPhoto()
                photo = gpsphoto.GPSPhoto(homedir + "/scans/" + filename +"/" + filename +"V.jpg")

                # Create GPSInfo Data Object to modify gps data to play well with Photogrammetry software
                info = gpsphoto.GPSInfo((coordinatevlongitudefloated, coordinatevlatitudefloated))
                info = gpsphoto.GPSInfo((coordinatevlongitudefloated, coordinatevlatitudefloated), \
                  timeStamp=current_time)
                info = gpsphoto.GPSInfo((coordinatevlongitudefloated, coordinatevlatitudefloated), \
                  alt=10, timeStamp=current_time)

                # Modify GPS Data and resave image
                photo.modGPSData(info, homedir + "/scans/" + filename +"/" + filename +"V.jpg")

                print("/scans/" + filename +"/" + filename +"V.jpg")
                print('resaved with modified GPS Meta data')

                # Taking picture with opencv
                videoCaptureObjectW = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret,frame23 = videoCaptureObjectW.read()
                    frame23 = cv2.rotate(frame23, cv2.ROTATE_180)
                    cv2.imwrite(homedir + "/scans/" + filename +"/" + filename +"W.jpg",frame23)
                    result = False
                videoCaptureObjectW.release()
                cv2.destroyAllWindows()
                logger.info(filename + "W.jpg captured located in: " + homedir + "/scans/" +filename)
                print(filename + "W.jpg captured located in: " + homedir + "/scans/" +filename)

                # Sends enough characters to turn the platform one quarter turn via the arduino hooked through serial connection
                platser.write('q1\n'.encode())
                
                print("motor rotated image taken")

                #sleep for 4 seconds allows arduino time before we send it another command
                time.sleep(4)

                print("modifying GPS data for play well with")
                # Create a GPSPhoto Object to modify gps data to play well with Photogrammetry software
                photo = gpsphoto.GPSPhoto()
                photo = gpsphoto.GPSPhoto(homedir + "/scans/" + filename +"/" + filename +"W.jpg")

                # Create GPSInfo Data Object to modify gps data to play well with Photogrammetry software
                info = gpsphoto.GPSInfo((coordinatewlongitudefloated, coordinatewlatitudefloated))
                info = gpsphoto.GPSInfo((coordinatewlongitudefloated, coordinatewlatitudefloated), \
                  timeStamp=current_time)
                info = gpsphoto.GPSInfo((coordinatewlongitudefloated, coordinatewlatitudefloated), \
                  alt=10, timeStamp=current_time)

                # Modify GPS Data and resave image
                photo.modGPSData(info, homedir + "/scans/" + filename +"/" + filename +"W.jpg")

                print("/scans/" + filename +"/" + filename +"W.jpg")
                print('resaved with modified GPS Meta data')

                # Taking picture with opencv
                videoCaptureObjectX = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret,frame24 = videoCaptureObjectX.read()
                    frame24 = cv2.rotate(frame24, cv2.ROTATE_180)
                    cv2.imwrite(homedir + "/scans/" + filename +"/" + filename +"X.jpg",frame24)
                    result = False
                videoCaptureObjectX.release()
                cv2.destroyAllWindows()
                logger.info(filename + "X.jpg captured located in: " + homedir + "/scans/" +filename)
                print(filename + "X.jpg captured located in: " + homedir + "/scans/" +filename)

                # Sends enough characters to turn the platform one quarter turn via the arduino hooked through serial connection
                platser.write('q1\n'.encode())
                
                print("motor rotated image taken")

                #sleep for 4 seconds allows arduino time before we send it another command
                time.sleep(4)

                print("modifying GPS data for play well with")
                # Create a GPSPhoto Object to modify gps data to play well with Photogrammetry software
                photo = gpsphoto.GPSPhoto()
                photo = gpsphoto.GPSPhoto(homedir + "/scans/" + filename +"/" + filename +"X.jpg")

                # Create GPSInfo Data Object to modify gps data to play well with Photogrammetry software
                info = gpsphoto.GPSInfo((coordinatexlongitudefloated, coordinatexlatitudefloated))
                info = gpsphoto.GPSInfo((coordinatexlongitudefloated, coordinatexlatitudefloated), \
                  timeStamp=current_time)
                info = gpsphoto.GPSInfo((coordinatexlongitudefloated, coordinatexlatitudefloated), \
                  alt=10, timeStamp=current_time)

                # Modify GPS Data and resave image
                photo.modGPSData(info, homedir + "/scans/" + filename +"/" + filename +"X.jpg")

                print("/scans/" + filename +"/" + filename +"X.jpg")
                print('resaved with modified GPS Meta data')
                time.sleep(3)
                logger.info('Local Scan Complete')
                logger.info('Creating Webpage for Scan')
                # create web page with images
                with open(homedir + "/scans/" + filename + "/" + filename +'.html', 'w') as file:
                    message = """<!DOCTYPE html>
                                <html>
                                <head>
                                <style>
                                div.gallery {
                                  margin: 5px;
                                  border: 1px solid #ccc;
                                  float: left;
                                  width: 180px;
                                }

                                div.gallery:hover {
                                  border: 1px solid #777;
                                }

                                div.gallery img {
                                  width: 100%;
                                  height: auto;
                                }

                                div.desc {
                                  padding: 15px;
                                  text-align: center;
                                }
                                </style>
                                </head>
                                <body>

                                <div class="gallery">
                                  <a target="_blank" href='./"""+ filename +"""A.jpg'>
                                    <img src='./"""+ filename +"""A.jpg' width="600" height="400">
                                  </a>
                                  <div class="desc">"""+ filename +"""A.jpg</div>
                                </div>


                                <div class="gallery">
                                  <a target="_blank" href='./"""+ filename +"""B.jpg'>
                                    <img src='./"""+ filename +"""B.jpg' width="600" height="400">
                                  </a>
                                  <div class="desc">"""+ filename +"""B.jpg</div>
                                </div>


                                <div class="gallery">
                                  <a target="_blank" href='./"""+ filename +"""C.jpg'>
                                    <img src='./"""+ filename +"""C.jpg' width="600" height="400">
                                  </a>
                                  <div class="desc">"""+ filename +"""C.jpg</div>
                                </div>


                                <div class="gallery">
                                  <a target="_blank" href='./"""+ filename +"""D.jpg'>
                                    <img src='./"""+ filename +"""D.jpg' width="600" height="400">
                                  </a>
                                  <div class="desc">"""+ filename +"""D.jpg</div>
                                </div>


                                <div class="gallery">
                                  <a target="_blank" href='./"""+ filename +"""E.jpg'>
                                    <img src='./"""+ filename +"""E.jpg' width="600" height="400">
                                  </a>
                                  <div class="desc">"""+ filename +"""E.jpg</div>
                                </div>


                                <div class="gallery">
                                  <a target="_blank" href='./"""+ filename +"""F.jpg'>
                                    <img src='./"""+ filename +"""F.jpg' width="600" height="400">
                                  </a>
                                  <div class="desc">"""+ filename +"""F.jpg</div>
                                </div>


                                <div class="gallery">
                                  <a target="_blank" href='./"""+ filename +"""G.jpg'>
                                    <img src='./"""+ filename +"""G.jpg' width="600" height="400">
                                  </a>
                                  <div class="desc">"""+ filename +"""G.jpg</div>
                                </div>


                                <div class="gallery">
                                  <a target="_blank" href='./"""+ filename +"""H.jpg'>
                                    <img src='./"""+ filename +"""H.jpg' width="600" height="400">
                                  </a>
                                  <div class="desc">"""+ filename +"""H.jpg</div>
                                </div>


                                <div class="gallery">
                                  <a target="_blank" href='./"""+ filename +"""I.jpg'>
                                    <img src='./"""+ filename +"""I.jpg' width="600" height="400">
                                  </a>
                                  <div class="desc">"""+ filename +"""I.jpg</div>
                                </div>


                                <div class="gallery">
                                  <a target="_blank" href='./"""+ filename +"""J.jpg'>
                                    <img src='./"""+ filename +"""J.jpg' width="600" height="400">
                                  </a>
                                  <div class="desc">"""+ filename +"""J.jpg</div>
                                </div>


                                <div class="gallery">
                                  <a target="_blank" href='./"""+ filename +"""K.jpg'>
                                    <img src='./"""+ filename +"""K.jpg' width="600" height="400">
                                  </a>
                                  <div class="desc">"""+ filename +"""K.jpg</div>
                                </div>


                                <div class="gallery">
                                  <a target="_blank" href='./"""+ filename +"""L.jpg'>
                                    <img src='./"""+ filename +"""L.jpg' width="600" height="400">
                                  </a>
                                  <div class="desc">"""+ filename +"""L.jpg</div>
                                </div>


                                <div class="gallery">
                                  <a target="_blank" href='./"""+ filename +"""M.jpg'>
                                    <img src='./"""+ filename +"""M.jpg' width="600" height="400">
                                  </a>
                                  <div class="desc">"""+ filename +"""M.jpg</div>
                                </div>


                                <div class="gallery">
                                  <a target="_blank" href='./"""+ filename +"""N.jpg'>
                                    <img src='./"""+ filename +"""N.jpg' width="600" height="400">
                                  </a>
                                  <div class="desc">"""+ filename +"""N.jpg</div>
                                </div>


                                <div class="gallery">
                                  <a target="_blank" href='./"""+ filename +"""O.jpg'>
                                    <img src='./"""+ filename +"""O.jpg' width="600" height="400">
                                  </a>
                                  <div class="desc">"""+ filename +"""O.jpg</div>
                                </div>


                                <div class="gallery">
                                  <a target="_blank" href='./"""+ filename +"""P.jpg'>
                                    <img src='./"""+ filename +"""P.jpg' width="600" height="400">
                                  </a>
                                  <div class="desc">"""+ filename +"""P.jpg</div>
                                </div>


                                <div class="gallery">
                                  <a target="_blank" href='./"""+ filename +"""Q.jpg'>
                                    <img src='./"""+ filename +"""Q.jpg' width="600" height="400">
                                  </a>
                                  <div class="desc">"""+ filename +"""Q.jpg</div>
                                </div>


                                <div class="gallery">
                                  <a target="_blank" href='./"""+ filename +"""R.jpg'>
                                    <img src='./"""+ filename +"""R.jpg' width="600" height="400">
                                  </a>
                                  <div class="desc">"""+ filename +"""R.jpg</div>
                                </div>


                                <div class="gallery">
                                  <a target="_blank" href='./"""+ filename +"""S.jpg'>
                                    <img src='./"""+ filename +"""S.jpg' width="600" height="400">
                                  </a>
                                  <div class="desc">"""+ filename +"""S.jpg</div>
                                </div>


                                <div class="gallery">
                                  <a target="_blank" href='./"""+ filename +"""T.jpg'>
                                    <img src='./"""+ filename +"""T.jpg' width="600" height="400">
                                  </a>
                                  <div class="desc">"""+ filename +"""T.jpg</div>
                                </div>


                                <div class="gallery">
                                  <a target="_blank" href='./"""+ filename +"""U.jpg'>
                                    <img src='./"""+ filename +"""U.jpg' width="600" height="400">
                                  </a>
                                  <div class="desc">"""+ filename +"""U.jpg</div>
                                </div>


                                <div class="gallery">
                                  <a target="_blank" href='./"""+ filename +"""V.jpg'>
                                    <img src='./"""+ filename +"""V.jpg' width="600" height="400">
                                  </a>
                                  <div class="desc">"""+ filename +"""V.jpg</div>
                                </div>


                                <div class="gallery">
                                  <a target="_blank" href='./"""+ filename +"""W.jpg'>
                                    <img src='./"""+ filename +"""W.jpg' width="600" height="400">
                                  </a>
                                  <div class="desc">"""+ filename +"""W.jpg</div>
                                </div>


                                <div class="gallery">
                                  <a target="_blank" href='./"""+ filename +"""X.jpg'>
                                    <img src='./"""+ filename +"""X.jpg' width="600" height="400">
                                  </a>
                                  <div class="desc">"""+ filename +"""X.jpg</div>
                                </div>


                        <div class=""><a href='./"""+ filename +""".zip'>Click here to download zip of all files</a></div>
                          </body>



                    </html>"""

                    file.write(message)
                    file.close()
                    logger.info('Webpage complete')
                    logger.info('Compresssing files to a zip')
                subprocess.Popen(["zip", "-r", homedir + "/scans/" +
                                filename + ".zip", homedir + "/scans/" + filename +"/"])
                time.sleep(10)
                logger.info('Files successfully compressed to zip file')
                logger.info('Attempting to connecting file server')                     
              
                # Using FTP and ftplib to connect to server and upload files we just created from scan
                severipasastring = str(serverip)
                
                ftp = FTP(severipasastring)  # connect to host, default port
                logger.info('Connection to server successful')
                myfilea = open(r'' + homedir + '/scans/' + filename +'/' + filename +'A.jpg', 'rb')
                myfileb = open(r'' + homedir + '/scans/' + filename +'/' + filename +'B.jpg', 'rb')
                myfilec = open(r'' + homedir + '/scans/' + filename +'/' + filename +'C.jpg', 'rb')
                myfiled = open(r'' + homedir + '/scans/' + filename +'/' + filename +'D.jpg', 'rb')
                myfilee = open(r'' + homedir + '/scans/' + filename +'/' + filename +'E.jpg', 'rb')
                myfilef = open(r'' + homedir + '/scans/' + filename +'/' + filename +'F.jpg', 'rb')
                myfileg = open(r'' + homedir + '/scans/' + filename +'/' + filename +'G.jpg', 'rb')
                myfileh = open(r'' + homedir + '/scans/' + filename +'/' + filename +'H.jpg', 'rb')
                myfilei = open(r'' + homedir + '/scans/' + filename +'/' + filename +'I.jpg', 'rb')
                myfilej = open(r'' + homedir + '/scans/' + filename +'/' + filename +'J.jpg', 'rb')
                myfilek = open(r'' + homedir + '/scans/' + filename +'/' + filename +'K.jpg', 'rb')
                myfilel = open(r'' + homedir + '/scans/' + filename +'/' + filename +'L.jpg', 'rb')
                myfilem = open(r'' + homedir + '/scans/' + filename +'/' + filename +'M.jpg', 'rb')
                myfilen = open(r'' + homedir + '/scans/' + filename +'/' + filename +'N.jpg', 'rb')
                myfileo = open(r'' + homedir + '/scans/' + filename +'/' + filename +'O.jpg', 'rb')
                myfilep = open(r'' + homedir + '/scans/' + filename +'/' + filename +'P.jpg', 'rb')
                myfileq = open(r'' + homedir + '/scans/' + filename +'/' + filename +'Q.jpg', 'rb')
                myfiler = open(r'' + homedir + '/scans/' + filename +'/' + filename +'R.jpg', 'rb')
                myfiles = open(r'' + homedir + '/scans/' + filename +'/' + filename +'S.jpg', 'rb')
                myfilet = open(r'' + homedir + '/scans/' + filename +'/' + filename +'T.jpg', 'rb')
                myfileu = open(r'' + homedir + '/scans/' + filename +'/' + filename +'U.jpg', 'rb')
                myfilev = open(r'' + homedir + '/scans/' + filename +'/' + filename +'V.jpg', 'rb')
                myfilew = open(r'' + homedir + '/scans/' + filename +'/' + filename +'W.jpg', 'rb')
                myfilex = open(r'' + homedir + '/scans/' + filename +'/' + filename +'X.jpg', 'rb')
                myfilezip = open(r'' + homedir + '/scans/' + filename +'.zip', 'rb')
                myfilehtml = open(r'' + homedir + '/scans/' + filename +'/' + filename +'.html', 'rb')
                if __name__ == "__main__":
                    ftp_host = severipasastring
                    username = serveruser
                    password = serverpassword
                try: ftp = FTP(host=ftp_host, user=username, passwd=password)
                except error_perm as e:
                    print("User credentials failed")
                    logger.warning('User credentials failed')
                else:
                    logger.info('Succesfully logged into file server')
                    ftp.cwd('/public_html/' + 'scans/')
                    ftp.storbinary('STOR ' + filename +'A.jpg', myfilea)
                    ftp.storbinary('STOR ' + filename +'B.jpg', myfileb)
                    ftp.storbinary('STOR ' + filename +'C.jpg', myfilec)
                    ftp.storbinary('STOR ' + filename +'D.jpg', myfiled)
                    ftp.storbinary('STOR ' + filename +'E.jpg', myfilee)
                    ftp.storbinary('STOR ' + filename +'F.jpg', myfilef)
                    ftp.storbinary('STOR ' + filename +'G.jpg', myfileg)
                    ftp.storbinary('STOR ' + filename +'H.jpg', myfileh)
                    ftp.storbinary('STOR ' + filename +'I.jpg', myfilei)
                    ftp.storbinary('STOR ' + filename +'J.jpg', myfilej)
                    ftp.storbinary('STOR ' + filename +'K.jpg', myfilek)
                    ftp.storbinary('STOR ' + filename +'L.jpg', myfilel)
                    ftp.storbinary('STOR ' + filename +'M.jpg', myfilem)
                    ftp.storbinary('STOR ' + filename +'N.jpg', myfilen)
                    ftp.storbinary('STOR ' + filename +'O.jpg', myfileo)
                    ftp.storbinary('STOR ' + filename +'P.jpg', myfilep)
                    ftp.storbinary('STOR ' + filename +'Q.jpg', myfileq)
                    ftp.storbinary('STOR ' + filename +'R.jpg', myfiler)
                    ftp.storbinary('STOR ' + filename +'S.jpg', myfiles)
                    ftp.storbinary('STOR ' + filename +'T.jpg', myfilet)
                    ftp.storbinary('STOR ' + filename +'U.jpg', myfileu)
                    ftp.storbinary('STOR ' + filename +'V.jpg', myfilev)
                    ftp.storbinary('STOR ' + filename +'W.jpg', myfilew)
                    ftp.storbinary('STOR ' + filename +'X.jpg', myfilex)
                    ftp.storbinary('STOR ' + filename +'.zip', myfilezip)
                    ftp.storbinary('STOR ' + filename +'.html', myfilehtml)
                    ftp.close()
                      
                      
                    # Uses SOX to play sound to let us know scan is complete
                    subprocess.call(["play", "finished.mp3", "--no-show-progress"])
                    logger.info('Scan susccesfully uploaded')
                    logger.info('Scan Complete')
                    print('Scan Complete')