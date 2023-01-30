#!/usr/bin/env python
"""config.py: this python script alters the configure file based off user input both from scans and entered data"""

__author__      = "Robert Moser"
__copyright__ = "Copyright 2023  Robert Moser"
__credits__ = ["myslef for now"]
__license__ = "GPL"
__version__ = "0.0.0"
__maintainer__ = "Robert Moser"
__email__ = "whyamisoawkward2021@gmail.com"
__status__ = "prototype"

from logging import NullHandler
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib
import configparser

builder = Gtk.Builder()
builder.add_from_file("./guifiles/config.glade")    
mainwindow = builder.get_object("configurewindow")
mainwindow.show_all()
config = configparser.ConfigParser()
config.read('settings.ini')

currentscan = config['currentscaninfo']['currentscan']
server_nicknameholder = config['serverinfo']['servernickname']
server_ipholder = config['serverinfo']['serveripaddress']
server_usernameholder = config['serverinfo']['serverusername']
server_passwordholder = config['serverinfo']['serverpassword']
scanner_nicknameholder = config['serverinfo']['scannernickname']
server_portholder = config['serverinfo']['serverportnumber']
coordinatealongitudeholder = config['coordinates']['coordinatealongitude'] 
coordinatealatitudeholder = config['coordinates']['coordinatealatitude']
coordinateblongitudeholder = config['coordinates']['coordinateblongitude'] 
coordinateblatitudeholder = config['coordinates']['coordinateblatitude']
coordinateclongitudeholder = config['coordinates']['coordinateclongitude'] 
coordinateclatitudeholder = config['coordinates']['coordinateclatitude']
coordinatedlongitudeholder = config['coordinates']['coordinatedlongitude'] 
coordinatedlatitudeholder = config['coordinates']['coordinatedlatitude']
coordinateelongitudeholder = config['coordinates']['coordinateelongitude'] 
coordinateelatitudeholder = config['coordinates']['coordinateelatitude']
coordinateflongitudeholder = config['coordinates']['coordinateflongitude'] 
coordinateflatitudeholder = config['coordinates']['coordinateflatitude']
coordinateglongitudeholder = config['coordinates']['coordinateglongitude'] 
coordinateglatitudeholder = config['coordinates']['coordinateglatitude']
coordinatehlongitudeholder = config['coordinates']['coordinatehlongitude'] 
coordinatehlatitudeholder = config['coordinates']['coordinatehlatitude']
coordinateilongitudeholder = config['coordinates']['coordinateilongitude'] 
coordinateilatitudeholder = config['coordinates']['coordinateilatitude']
coordinatejlongitudeholder = config['coordinates']['coordinatejlongitude'] 
coordinatejlatitudeholder = config['coordinates']['coordinatejlatitude']
coordinateklongitudeholder = config['coordinates']['coordinateklongitude'] 
coordinateklatitudeholder = config['coordinates']['coordinateklatitude']
coordinatellongitudeholder = config['coordinates']['coordinatellongitude'] 
coordinatellatitudeholder = config['coordinates']['coordinatellatitude']
coordinatemlongitudeholder = config['coordinates']['coordinatemlongitude'] 
coordinatemlatitudeholder = config['coordinates']['coordinatemlatitude']
coordinatenlongitudeholder = config['coordinates']['coordinatenlongitude'] 
coordinatenlatitudeholder = config['coordinates']['coordinatenlatitude']
coordinateolongitudeholder = config['coordinates']['coordinateolongitude'] 
coordinateolatitudeholder = config['coordinates']['coordinateolatitude']
coordinateplongitudeholder = config['coordinates']['coordinateplongitude'] 
coordinateplatitudeholder = config['coordinates']['coordinateplatitude']
coordinateqlongitudeholder = config['coordinates']['coordinateqlongitude'] 
coordinateqlatitudeholder = config['coordinates']['coordinateqlatitude']
coordinaterlongitudeholder = config['coordinates']['coordinaterlongitude'] 
coordinaterlatitudeholder = config['coordinates']['coordinaterlatitude']
coordinateslongitudeholder = config['coordinates']['coordinateslongitude'] 
coordinateslatitudeholder = config['coordinates']['coordinateslatitude']
coordinatetlongitudeholder = config['coordinates']['coordinatetlongitude'] 
coordinatetlatitudeholder = config['coordinates']['coordinatetlatitude']
coordinateulongitudeholder = config['coordinates']['coordinateulongitude'] 
coordinateulatitudeholder = config['coordinates']['coordinateulatitude']
coordinatevlongitudeholder = config['coordinates']['coordinatevlongitude'] 
coordinatevlatitudeholder = config['coordinates']['coordinatevlatitude']
coordinatewlongitudeholder = config['coordinates']['coordinatewlongitude'] 
coordinatewlatitudeholder = config['coordinates']['coordinatewlatitude']
coordinatexlongitudeholder = config['coordinates']['coordinatexlongitude'] 
coordinatexlatitudeholder = config['coordinates']['coordinatexlatitude']
passwordcount = len(server_passwordholder)
class mysupercoolhandlerforglade:          
        
        # Here we are telling the program that when the button saveconfig is pressed to use configure parser to save ini file
        def saveconfig(self, button, data=None):
                        config['serverinfo'] = {'servernickname': servernickname.get_text(),
                                                'serveripaddress': serverip.get_text(),
                                                'serverusername': serverusername.get_text(),
                                                'serverpassword': serverpassword.get_text(),
                                                'scannernickname': scannernickname.get_text(),
                                                'serverportnumber': serverport.get_text()}
                        
                        config['currentscaninfo'] = {'currentscan': currentscan}
                        
                        config['coordinates'] = {'coordinatealongitude': coordinatealongitude.get_text(),
                                                'coordinatealatitude': coordinatealatitude.get_text(),
                                                'coordinateblongitude': coordinateblongitude.get_text(),
                                                'coordinateblatitude': coordinateblatitude.get_text(),
                                                'coordinateclongitude': coordinateclongitude.get_text(),
                                                'coordinateclatitude': coordinateclatitude.get_text(),
                                                'coordinatedlongitude': coordinatedlongitude.get_text(),
                                                'coordinatedlatitude': coordinatedlatitude.get_text(),
                                                'coordinateelongitude': coordinateelongitude.get_text(),
                                                'coordinateelatitude': coordinateelatitude.get_text(),
                                                'coordinateflongitude': coordinateflongitude.get_text(),
                                                'coordinateflatitude': coordinateflatitude.get_text(),
                                                'coordinateglongitude': coordinatehlongitude.get_text(),
                                                'coordinateglatitude': coordinatehlatitude.get_text(),
                                                'coordinatehlongitude': coordinateilongitude.get_text(),
                                                'coordinatehlatitude': coordinateilatitude.get_text(),
                                                'coordinateilongitude': coordinatejlongitude.get_text(),
                                                'coordinateilatitude': coordinatejlatitude.get_text(),
                                                'coordinatejlongitude': coordinatejlongitude.get_text(),
                                                'coordinatejlatitude': coordinateklatitude.get_text(),
                                                'coordinateklongitude': coordinatellongitude.get_text(),
                                                'coordinateklatitude': coordinatellatitude.get_text(),
                                                'coordinatellongitude': coordinatellongitude.get_text(),
                                                'coordinatellatitude': coordinatellatitude.get_text(),
                                                'coordinatemlongitude': coordinatemlongitude.get_text(),
                                                'coordinatemlatitude': coordinatemlatitude.get_text(),
                                                'coordinatenlongitude': coordinatenlongitude.get_text(),
                                                'coordinatenlatitude': coordinatenlatitude.get_text(),
                                                'coordinateolongitude': coordinateolongitude.get_text(),
                                                'coordinateolatitude': coordinateolatitude.get_text(),
                                                'coordinateplongitude': coordinateplongitude.get_text(),
                                                'coordinateplatitude': coordinateplatitude.get_text(),
                                                'coordinateqlongitude': coordinateqlongitude.get_text(),
                                                'coordinateqlatitude': coordinateqlatitude.get_text(),
                                                'coordinaterlongitude': coordinaterlongitude.get_text(),
                                                'coordinaterlatitude': coordinaterlatitude.get_text(),
                                                'coordinateslongitude': coordinateslongitude.get_text(),
                                                'coordinateslatitude': coordinateslatitude.get_text(),
                                                'coordinatetlongitude': coordinatetlongitude.get_text(),
                                                'coordinatetlatitude': coordinatetlatitude.get_text(),
                                                'coordinateulongitude': coordinateulongitude.get_text(),
                                                'coordinateulatitude': coordinateulatitude.get_text(),
                                                'coordinatevlongitude': coordinatevlongitude.get_text(),
                                                'coordinatevlatitude': coordinatevlatitude.get_text(),
                                                'coordinatewlongitude': coordinatewlongitude.get_text(),
                                                'coordinatewlatitude': coordinatewlatitude.get_text(),
                                                'coordinatexlongitude': coordinatexlongitude.get_text(),
                                                'coordinatexlatitude': coordinatexlatitude.get_text()}
                        
                        with open('settings.ini', 'w') as configfile:
                                config.write(configfile)
                        
                        Gtk.main_quit()
        
        # closes without saving when user clicks cancel
        def cancelbutton(self, *args):
                        Gtk.main_quit(*args)

        
        
        
        def onDeleteWindow(self, *args):
                        Gtk.main_quit(*args)


# Sets up vairables to receive user in put from gtk

servernickname = builder.get_object("server_nickname")
servernickname.set_placeholder_text(server_nicknameholder)
serverip = builder.get_object("server_ip")
serverip.set_placeholder_text(server_ipholder)
serverusername = builder.get_object("server_username")
serverusername.set_placeholder_text(server_usernameholder)
serverpassword = builder.get_object("server_password")
serverpassword.set_placeholder_text(passwordcount*"*")
scannernickname = builder.get_object("scanner_nickname")
scannernickname.set_placeholder_text(scanner_nicknameholder)
serverport = builder.get_object("server_port")
serverport.set_placeholder_text(server_portholder)
coordinatealongitude = builder.get_object("coordinatealongitude")
coordinatealatitude = builder.get_object("coordinatealatitude")
coordinateblongitude = builder.get_object("coordinateblongitude")
coordinateblatitude = builder.get_object("coordinateblatitude")
coordinateclongitude = builder.get_object("coordinateclongitude")
coordinateclatitude = builder.get_object("coordinateclatitude")
coordinatedlongitude = builder.get_object("coordinatedlongitude")
coordinatedlatitude = builder.get_object("coordinatedlatitude")
coordinateelongitude = builder.get_object("coordinateelongitude")
coordinateelatitude = builder.get_object("coordinateelatitude")
coordinateflongitude = builder.get_object("coordinateflongitude")
coordinateflatitude = builder.get_object("coordinateflatitude")
coordinateglongitude = builder.get_object("coordinateglongitude")
coordinateglatitude = builder.get_object("coordinateglatitude")
coordinatehlongitude = builder.get_object("coordinatehlongitude")
coordinatehlatitude = builder.get_object("coordinatehlatitude")
coordinateilongitude = builder.get_object("coordinateilongitude")
coordinateilatitude = builder.get_object("coordinateilatitude")
coordinatejlongitude = builder.get_object("coordinatejlongitude")
coordinatejlatitude = builder.get_object("coordinatejlatitude")
coordinateklongitude = builder.get_object("coordinateklongitude")
coordinateklatitude = builder.get_object("coordinateklatitude")
coordinatellongitude = builder.get_object("coordinatellongitude")
coordinatellatitude = builder.get_object("coordinatellatitude")
coordinatemlongitude = builder.get_object("coordinatemlongitude")
coordinatemlatitude = builder.get_object("coordinatemlatitude")
coordinatenlongitude = builder.get_object("coordinatenlongitude")
coordinatenlatitude = builder.get_object("coordinatenlatitude")
coordinateolongitude = builder.get_object("coordinateolongitude")
coordinateolatitude = builder.get_object("coordinateolatitude")
coordinateplongitude = builder.get_object("coordinateplongitude")
coordinateplatitude = builder.get_object("coordinateplatitude")
coordinateqlongitude = builder.get_object("coordinateqlongitude")
coordinateqlatitude = builder.get_object("coordinateqlatitude")
coordinaterlongitude = builder.get_object("coordinaterlongitude")
coordinaterlatitude = builder.get_object("coordinaterlatitude")
coordinateslongitude = builder.get_object("coordinateslongitude")
coordinateslatitude = builder.get_object("coordinateslatitude")
coordinatetlongitude = builder.get_object("coordinatetlongitude")
coordinatetlatitude = builder.get_object("coordinatetlatitude")
coordinateulongitude = builder.get_object("coordinateulongitude")
coordinateulatitude = builder.get_object("coordinateulatitude")
coordinatevlongitude = builder.get_object("coordinatevlongitude")
coordinatevlatitude = builder.get_object("coordinatevlatitude")
coordinatewlongitude = builder.get_object("coordinatewlongitude")
coordinatewlatitude= builder.get_object("coordinatewlatitude")
coordinatexlongitude = builder.get_object("coordinatexlongitude")
coordinatexlatitude = builder.get_object("coordinatexlatitude")

coordinatealongitude.set_placeholder_text(coordinatealongitudeholder)
coordinatealatitude.set_placeholder_text(coordinatealatitudeholder)
coordinateblongitude.set_placeholder_text(coordinateblongitudeholder)
coordinateblatitude.set_placeholder_text(coordinateblatitudeholder)
coordinateclongitude.set_placeholder_text(coordinateclongitudeholder)
coordinateclatitude.set_placeholder_text(coordinateclatitudeholder)
coordinatedlongitude.set_placeholder_text(coordinatedlongitudeholder)
coordinatedlatitude.set_placeholder_text(coordinatedlatitudeholder)
coordinateelongitude.set_placeholder_text(coordinateelongitudeholder)
coordinateelatitude.set_placeholder_text(coordinateelatitudeholder)
coordinateflongitude.set_placeholder_text(coordinateflongitudeholder)
coordinateflatitude.set_placeholder_text(coordinateflatitudeholder)
coordinateglongitude.set_placeholder_text(coordinateglongitudeholder)
coordinateglatitude.set_placeholder_text(coordinateglatitudeholder)
coordinatehlongitude.set_placeholder_text(coordinatehlongitudeholder)
coordinatehlatitude.set_placeholder_text(coordinatehlatitudeholder)
coordinateilongitude.set_placeholder_text(coordinateilongitudeholder)
coordinateilatitude.set_placeholder_text(coordinateilatitudeholder)
coordinatejlongitude.set_placeholder_text(coordinatejlongitudeholder)
coordinatejlatitude.set_placeholder_text(coordinatejlatitudeholder)
coordinateklongitude.set_placeholder_text(coordinateklongitudeholder)
coordinateklatitude.set_placeholder_text(coordinateklatitudeholder)
coordinatellongitude.set_placeholder_text(coordinatellongitudeholder)
coordinatellatitude.set_placeholder_text(coordinatellatitudeholder)
coordinatemlongitude.set_placeholder_text(coordinatemlongitudeholder)
coordinatemlatitude.set_placeholder_text(coordinatemlatitudeholder)
coordinatenlongitude.set_placeholder_text(coordinatenlongitudeholder)
coordinatenlatitude.set_placeholder_text(coordinatenlatitudeholder)
coordinateolongitude.set_placeholder_text(coordinateolongitudeholder)
coordinateolatitude.set_placeholder_text(coordinateolatitudeholder)
coordinateplongitude.set_placeholder_text(coordinateplongitudeholder)
coordinateplatitude.set_placeholder_text(coordinateplatitudeholder)
coordinateqlongitude.set_placeholder_text(coordinateqlongitudeholder)
coordinateqlatitude.set_placeholder_text(coordinateqlatitudeholder)
coordinaterlongitude.set_placeholder_text(coordinaterlongitudeholder)
coordinaterlatitude.set_placeholder_text(coordinaterlatitudeholder)
coordinateslongitude.set_placeholder_text(coordinateslongitudeholder)
coordinateslatitude.set_placeholder_text(coordinateslatitudeholder)
coordinatetlongitude.set_placeholder_text(coordinatetlongitudeholder)
coordinatetlatitude.set_placeholder_text(coordinatetlatitudeholder)
coordinateulongitude.set_placeholder_text(coordinateulongitudeholder)
coordinateulatitude.set_placeholder_text(coordinateulatitudeholder)
coordinatevlongitude.set_placeholder_text(coordinatevlongitudeholder)
coordinatevlatitude.set_placeholder_text(coordinatevlatitudeholder)
coordinatewlongitude.set_placeholder_text(coordinatewlongitudeholder)
coordinatewlatitude.set_placeholder_text(coordinatewlatitudeholder)
coordinatexlongitude.set_placeholder_text(coordinatexlongitudeholder)
coordinatexlatitude.set_placeholder_text(coordinatexlatitudeholder)


# This is a class handler that connects to glades signals

builder.connect_signals(mysupercoolhandlerforglade()) 

Gtk.main()
