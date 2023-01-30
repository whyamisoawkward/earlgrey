#!/usr/bin/env python
"""failedseqdaigbox.py: dialog box for incorrectly stored sequence data"""

__author__      = "Robert Moser"
__copyright__ = "Copyright 2023  Robert Moser"
__credits__ = ["myslef for now"]
__license__ = "GPL"
__version__ = "0.0.0"
__maintainer__ = "Robert Moser"
__email__ = "whyamisoawkward2021@gmail.com"
__status__ = "prototype"

import gi
import logging
import os
import threading
import yaml
import cv2
import numpy as np
import subprocess
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib, GdkPixbuf

class Handler:

    def  okbtn(self, *args): 
        f = open("./seq.yaml", "w")
        f.write('---\n')
        f.write('''savedsequences: ''')
        f.write("""''""")
        f.close()
        print('Sequence file fixed please restart Earlgrey')   
        Gtk.main_quit(*args)
        
    def cancelbtn(self, *args):
        Gtk.main_quit(*args)

    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

builder = Gtk.Builder()
builder.add_from_file("./guifiles/failedsequencediagbox.glade")    
mainwindow = builder.get_object("mainwindow")
window = builder.get_object("window1")
mainwindow.show_all()
builder.connect_signals(Handler())   
Gtk.main()



