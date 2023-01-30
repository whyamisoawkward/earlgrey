#!/usr/bin/env python
"""This is the main program that sets the the sequence and scan data recorded by the user"""

__author__      = "Robert Moser"
__copyright__ = "Copyright 2023  Robert Moser"
__credits__ = ["myslef for now"]
__license__ = "GPL"
__version__ = "0.0.0"
__maintainer__ = "Robert Moser"
__email__ = "whyamisoawkward2021@gmail.com"
__status__ = "prototype"

import gi
import sys
import configparser
import logging
import os
import serial
import threading
import yaml
import cv2
import numpy as np
import subprocess
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib, GdkPixbuf
import datetime
from pathlib import Path
from monitorsequence import *
import time



# calling functions
start_time = time.time()
display_time = 2


#setups the "info"
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('./logs/earlgrey.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the file handler to the logger
logger.addHandler(handler)


# these define which serial ports are where. Make sure to set these to connect to the same serial ports everytime or you will have to reconfigure this code everytime. 

# If you are not sure which stepper is connected to which port you can send the command "idstepper" to that port and it will tell you which axis you are conected to. 
# This function will be removed when I migrate to a single mega 2560 
zaxisser = serial.Serial('/dev/ttyACM0', 115200)
yaxisser = serial.Serial('/dev/ttyACM0', 115200)
tiltser = serial.Serial('/dev/ttyACM0', 115200)
panser = serial.Serial('/dev/ttyACM0', 115200)
platser = serial.Serial('/dev/ttyACM0', 115200)

# this is just to check to see if the yaml file is sctured correctly 
# if for some reason it doesn't load the sequence file
# it returns a dialog box with options for the user to either delete or
# load another sequence in it's placeL
try:
# Referencing our YMAL file
    yaml_file = 'seq.yaml' # key: value
    # Openning our YAML file
    with open(yaml_file, 'r') as fh:
        python_object = yaml.load(fh, Loader=yaml.SafeLoader)
except:
    logger.error('Could not load properly load sequence from seq.yaml')
    print('Could not load properly load sequence from seq.yaml')
    def callbackforfailedsequence():
            os.system("python3 dialogboxes/failedseqdaigbox.py")
    t = threading.Thread(target=callbackforfailedsequence)
    t.start()



        

# Pulls saved sequence from yaml file and converts it to a varaiable we can use in python
saved_sequences = python_object['savedsequences']


cap = cv2.VideoCapture(0)
cap.open("/dev/v4l/by-id/usb-USB_Camera_USB_Camera_SN0001-video-index0")

config = configparser.ConfigParser()
config.read('settings.ini')

comparetocurrentscan = config['currentscaninfo']['currentscan']
comparetocurrentscantest = config['currentscaninfo']['currentscan']
server_nickname = config['serverinfo']['servernickname']
scanner_nickname = config['serverinfo']['scannernickname']
makesurenotempty = ('empty')

def cleanoutcharacters(removecharacterfun, X):

    # Base Case
    if (len(removecharacterfun) == 0):
        return ''

    # Check the first character of removecharacterfuning
    if (removecharacterfun[0] == X):

        # Pass the rest of the removecharacterfuning to recursion Function call
        return cleanoutcharacters(removecharacterfun[1:], X)

    # Add the first character of removecharacterfun and removecharacterfuning from recursion
    return removecharacterfun[0] + cleanoutcharacters(removecharacterfun[1:], X)

# this feeds the output from yaml to the recursion code
# now the removecharacterfun is repesented by what we pulled from the YAML
removecharacterfun = saved_sequences

# characters we are removing from the output so that it will play nicely with the input 
# on arduino that runs the motor on the scanner
X = ','

# Function call to clear out set characters
removecharacterfun = cleanoutcharacters(removecharacterfun, X)

# Using replace to replace charaters I want to represent. Here we are replacing the character 'r' for a '\n' (a return signal) to the arduino
characterreplacefunc = (removecharacterfun.replace('r', '\n'))
charactercount = (len(characterreplacefunc))      
charactercountfloated = charactercount

# We need to divide the counted chacraters to deermine the lenght of the recorded sequence but we needed to float the number to allow this
float(charactercountfloated)
# heres the actual divding and given a variable we can use
dividedby3 = (charactercountfloated/3)
amountofstepsinsequence = str(dividedby3) 

# This takes the amount of steps already recorded in the current sequence and adds 1 to it everytime a step button is pressed
# to give the user a live look at how many steps are in the sequence
stepcounterdisplay = 0 + float(amountofstepsinsequence)

# asking for user input
search_word_count = ('spr')


# reading data of the file
read_data = saved_sequences

# counting the occurrence 
word_count = read_data.count(search_word_count)
scanpointsdisplay = word_count
print(word_count)


builder = Gtk.Builder()
builder.add_from_file("./guifiles/earlgrey.glade")    
mainwindow = builder.get_object("mainwindow")
window = builder.get_object("window1")
stackwindowright = builder.get_object("stackwindowright")
showviewport = builder.get_object("showviewport")
showprogress = builder.get_object("showprogress")
showfinished = builder.get_object("showfinished")
spinner = builder.get_object("spinner")
image = builder.get_object("viewport")
currentscan = builder.get_object("currentscantxt")
statusbar1 = builder.get_object("statusbar1")
statusbar2 = builder.get_object("statusbar2")
context_id1 = statusbar1.get_context_id("status1")
context_id2 = statusbar2.get_context_id("status2")
mainwindow.show_all()


tripshowprogress = showprogress
checkbutton = Gtk.CheckButton("Click me!")
        
class StackSwitcher(Gtk.Window):        
    
    def stackwindowright1(stackwindowright):
        
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=100)
        stackwindowright.add(vbox)

        stack = stackwindowright
        
        
        stack(showviewport)
        stack(checkbutton)
        stack(showprogress)
        
        stack(showfinished,"showviewportpage", "showviewport")

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)
        vbox.pack_start(stack_switcher, True, True, 0)
        vbox.pack_start(stack, True, True, 0)
        
class Handler:

    
    
    def show_frame(*args):
        try:
            # where my text is going show up on the screen
            
            dt = str(datetime.datetime.now())
            org = (50, 20)
            org2 = (435, 470)
            # font of my text
            fontScale = .59
            fontScale2 = .40
            
            # Color of my text
            color = (255, 0, 0)
            
            # Line thickness of 2 px
            thickness = 1
            font = cv2.FONT_HERSHEY_SIMPLEX
            ret, frame = cap.read()
            frame = cv2.resize(frame, None, fx=1, fy=1, interpolation = cv2.INTER_CUBIC)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.flip(frame,-1)
            frame = cv2.putText(frame, 'Current sequence has ' + str(stepcounterdisplay) + ' steps and ' + str(scanpointsdisplay)  + ' scanpoints', org, font, 
                            fontScale, color, thickness, cv2.LINE_AA)
            frame = cv2.putText(frame, dt,org2,font,
                                fontScale2, color, thickness, cv2.LINE_AA)
            
        
            # put the dt variable over the
            # video frame

            
            pb = GdkPixbuf.Pixbuf.new_from_data(frame.tostring(),
                                            GdkPixbuf.Colorspace.RGB,
                                            False,
                                            8,
                                            frame.shape[1],
                                            frame.shape[0],
                                            frame.shape[2]*frame.shape[1])
            image.set_from_pixbuf(pb.copy())
            return True
        except Exception as e:
            print('Camera could not be loaded into opencv.')

    GLib.idle_add(show_frame)
    
    
        
        

    def  zup4(self, button):
        global stepcounterdisplay
        stepcounterdisplay += 1
        print(stepcounterdisplay)
        # sends serial data to arduino to tell driver to move motor
        zaxisser.write('u4\n'.encode())
        # adds step to sequence file
        f = open("seq.yaml", "a")
        f.write('''u4r,''')
        f.close()
        
        
        
            
    
        
    def  zdown4(self, button):
        
        global stepcounterdisplay
        
        stepcounterdisplay += 1
        print(stepcounterdisplay)
        # sends serial data to arduino to tell driver to move motor
        zaxisser.write('d4\n'.encode())
        
        # adds step to sequence file
        f = open("seq.yaml", "a")
        f.write('''d4r,''')
        f.close()

        
    def  ybackwards(self, button):
        
        global stepcounterdisplay
        
        stepcounterdisplay += 1
        print(stepcounterdisplay)
        # sends serial data to arduino to tell driver to move motor
        yaxisser.write('b4\n'.encode())
        
        # adds step to sequence file
        f = open("seq.yaml", "a")
        f.write('''b4r,''')
        f.close()
    

    def  yforward(self, button):
        
        global stepcounterdisplay
        
        stepcounterdisplay += 1
        print(stepcounterdisplay)
        
        # sends serial data to arduino to tell driver to move motor
        yaxisser.write('f4\n'.encode())
        
        # adds step to sequence file
        f = open("seq.yaml", "a")
        f.write('''f4r,''')
        f.close()
    
    def  rotateplatform(self, button):
        
        global stepcounterdisplay
        
        stepcounterdisplay += 1
        print(stepcounterdisplay)
        
        # sends serial data to arduino to tell driver to move motor
        yaxisser.write('b4\n'.encode())
        
        # adds step to sequence file
        f = open("seq.yaml", "a")
        f.write('''q4r,''')
        f.close()

        
    def  tiltup(self, button):
        
        global stepcounterdisplay
        
        stepcounterdisplay += 1
        print(stepcounterdisplay)
        
        # sends serial data to arduino to tell driver to move motor
        tiltser.write('s1\n'.encode())
        
        ## adds step to sequence file
        f = open("seq.yaml", "a")
        f.write('''s1r,''')
        f.close()
    
        
    def  tiltdown(self, button):
        
        global stepcounterdisplay
        
        stepcounterdisplay += 1
        print(stepcounterdisplay)
    
        # sends serial data to arduino to tell driver to move motor
        tiltser.write('i1\n'.encode())
        
        # adds step to sequence file
        f = open("seq.yaml", "a")
        f.write('''i1r,''')
        f.close()
    
        
    def  panleft(self, button):
        
        global stepcounterdisplay
        
        stepcounterdisplay += 1
        print(stepcounterdisplay)
        
        # sends serial data to arduino to tell driver to move motor
        panser.write('y1\n'.encode())
        
        # adds step to sequence file
        f = open("seq.yaml", "a")
        f.write('''y1r,''')
        f.close()
    
        
    def  panright(self, button):
        
        global stepcounterdisplay
        
        stepcounterdisplay += 1
        print(stepcounterdisplay)
        
        # sends serial data to arduino to tell driver to move motor
        panser.write('x1\n'.encode())
        
        # adds step to sequence file
        f = open("seq.yaml", "a")
        f.write('''x1r,''')
        f.close()
    
        
    def  markposition(self, button):
        global scanpointsdisplay
        scanpointsdisplay += 1
        # adds marker for scanning
        f = open("seq.yaml", "a")
        f.write('''spr,''')
        f.close()
        
    # rotates platform to help get object on scanner into postion    
    def  rotateplatform(self, button):
        platser.write('q1\n'.encode())
        
        
    #runs a 360  full rotation scan from current postion and uploads it to a configured server of your choosing     
    def  endsquence(self, button):   
        def callbackforstartsequence():
            os.system("python3 dialogboxes/savesequencediag.py")
        t = threading.Thread(target=callbackforstartsequence)
        t.start()
        
    
    def  startsequence(self, button):
        global stepcounterdisplay
        global scanpointsdisplay
        stepcounterdisplay = 0
        scanpointsdisplay = 0
        print(stepcounterdisplay)
        
        def callbackforstartsequence():
            
            os.system("python3 dialogboxes/startsequencediag.py")
        t = threading.Thread(target=callbackforstartsequence)
        t.start()

        
    def  runsequence(self, button,*args):
        def callbackforrunsequence():
            os.system("python3 runsequence.py")
        t = threading.Thread(target=callbackforrunsequence)
        t.start()
    
    def  aboutbtn(self, button):
        def callbackforabout():
            os.system("python3 dialogboxes/about.py")
        t = threading.Thread(target=callbackforabout)
        t.start()
        
    def  scanposition(self, button):
        
        cap.release()   
        cv2.destroyAllWindows()
        def callbackforscanpos():                          
            config['currentscaninfo'] = {'currentscan': currentscan.get_text() }
            with open('settings.ini', 'w') as configfile:
                config.write(configfile)
            process = subprocess.Popen([sys.executable, "dialogboxes/scanpos.py"])
            process.communicate()
            process.wait()
        t = threading.Thread(target=callbackforscanpos)
        t.start()

    def  preferences(self, button):
        def callback():
            os.system("python3 config.py")
        t = threading.Thread(target=callback)
        t.start()

    
    def quitbtn(self, *args):
        Gtk.main_quit(*args)
        
    
    
    def onDeleteWindow(self, button):
        self.quit()
            

builder.connect_signals(Handler())   
statusbar1.push(context_id1, 'Server: ' + server_nickname,)
statusbar2.push(context_id2, 'User: ' + scanner_nickname,)

Gtk.main()
