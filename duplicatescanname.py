#!/usr/bin/env python
"""duplicatescanname.py: simple dialog box to let the user know they have a previous scan with the same name"""

__author__      = "Robert Moser"
__copyright__ = "Copyright 2023  Robert Moser"
__credits__ = ["myslef for now"]
__license__ = "GPL"
__version__ = "0.0.0"
__maintainer__ = "Robert Moser"
__email__ = "whyamisoawkward2021@gmail.com"
__status__ = "prototype"

import gi
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

config = configparser.ConfigParser()
config.read('settings.ini')
currentscan = config['currentscaninfo']['currentscan']
print(currentscan)
class Handler:

   def  okbtn(self, button):
      () 
   def cancelbtn(self, *args):
      Gtk.main_quit(*args)

   def onDeleteWindow(self, *args):
      Gtk.main_quit(*args)

builder = Gtk.Builder()
builder.add_from_file("./guifiles/duplicatescanname.glade")    
mainwindow = builder.get_object("mainwindow")
window = builder.get_object("window1")
statusbar1 = builder.get_object("statusbar1")
context_id1 = statusbar1.get_context_id("status1")
statusbar1.push(context_id1, 'An previous scan with the name ' + currentscan + ' already exists in your filesystem. Would you like to overwrite?',)
mainwindow.show_all()
builder.connect_signals(Handler())   
Gtk.main()



