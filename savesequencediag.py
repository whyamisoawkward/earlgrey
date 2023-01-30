#!/usr/bin/env python
#!/usr/bin/env python
"""savesquencediag.py: saves sequence data"""

__author__      = "Robert Moser"
__copyright__ = "Copyright 2023  Robert Moser"
__credits__ = ["myslef for now"]
__license__ = "GPL"
__version__ = "0.0.0"
__maintainer__ = "Robert Moser"
__email__ = "whyamisoawkward2021@gmail.com"
__status__ = "prototype"

import gi
import subprocess
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib, GdkPixbuf

class Handler:
    
    def  okbtn(self, *args): 
        f = open("./seq.yaml", "a")
        f.write("""'""")
        f.close()  
        Gtk.main_quit(*args)
        
    def  cancelbtn(self, *args):
        Gtk.main_quit(*args)
        
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)


builder = Gtk.Builder()
builder.add_from_file("./guifiles/savesequencediag.glade")    
mainwindow = builder.get_object("mainwindow")
window = builder.get_object("window1")
image = builder.get_object("viewport")
mainwindow.show_all()
builder.connect_signals(Handler())   

Gtk.main()
