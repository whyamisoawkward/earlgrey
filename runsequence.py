#!/usr/bin/env python3

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
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib, GdkPixbuf
import serial
import datetime
import yaml
from time import sleep
import time
import configparser
import os.path
import logging
from subprocess import Popen
import threading, queue

#setups the 'info'
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#setups the 'info'
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('./logs/runsequence.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the file handler to the logger
logger.addHandler(handler)
current_time = datetime.datetime.now()






# Setting up a serial connection between the Arduino 
arduino = serial.Serial('/dev/ttyACM0', 115200, timeout=1)


    

    
# Referencing our YMAL file
yaml_file = 'seq.yaml' # key: value
# Openning our YAML file
with open(yaml_file, 'r') as fh:
    python_object = yaml.load(fh, Loader=yaml.SafeLoader)




# Pulls saved sequence from yaml file and converts it to a varaiable we can use in python
saved_sequences = python_object['savedsequences']

# This function is used to remove a unwanted characters in this case a comma
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

#needed to handle if the sequence only has one step
if dividedby3 < 2:
    print('\n')
    print('Squences has only 1 step')
    logger.info('Sequence started with only when 1 step')
    
else:
    print('\n')
    print('Recorded sequence has',dividedby3,'steps\n')

# splits strings into chunks allowing me to to make each chunk 4 characters long (exact length of our commands to the Arduino)
# we then send this to the iterator to spit out each command in between a time sleep function
# this prevents the computer or pi from sending all the data from the YAML file at once.
str = characterreplacefunc
n = 3
chunks = [str[i:i+n] for i in range(0, len(str), n)]

stepscounted = dividedby3




# converting the list to an iterator
iteratorloop = iter(chunks)
print('Sequence started')
logger.info('%s Step sequence started',stepscounted)



# Here we are using iterate to cycle through all of the steps stored in YAML
# Took a simple loop and set it to stop at however many steps are stored in the sequence files
# by counting the characters in that line. Then chopping the characters up by 4 (should do it by commas but whatever for now I guess).
# Quick side note. So iterator needs '(next' or it will push back something like '<list_iterator  # object at 0x7f19e0f49d60>'
# in short iterators need to iterate or they won't work. 



a = b = 1
while (a<(dividedby3)+1):
    arduino.write(next(iteratorloop).encode())
    print('Step',a,'taken')
    logger.info('%s steps taken',a)
    time.sleep(0.5)
    a = a + 1
    b = b + 1
    if (b == dividedby3):
        ()
else:
    print('Sequence complete')
    logger.info('Sequence Complete')
    
# so now that we got this figured out. your script works as long as the 
# chopped up chunks  from each string line up with what you feed your interatorloop
