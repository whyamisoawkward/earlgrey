README 	Prototype software for fully automated 3d scanner


AUTHORS 	Robert Moser



CHANGELOG 	

[0.0.0]
(10-19-2021)

* Currently I’m working on making a test hand shake script for the scanner that allows the scanner to run from sequence’s stored in YAML

*  I’ve figured out how to remove the unneeded characters from the YAML file for each sequence stored and send into the scanner. My problem now is that  I need to create timeout from each interpreted step sent to the scanner. I think the best way to do this is use a simple hand shake script that confirms each step.

	We can then use it to do 2 things, 1: Incorporate some logging system to allow for further automation of debugging. 2: Allow for handling of the timeout we need from the python script to scanner. (I’m still fuzzy on this because sending a return between each sequence now allows to run a step for each line but I need each sequence to remain on one line. Currently I’m using a recursive function to remove the commas from the data. I also using the “replace” function to replace letters to represent a carriage return “/n”.  that way we can record sequences wit minimal clutter for the scanner to run from YAML. 

		--- Side note to self: A tutorial suggests also creating a handler to throw away blank lines if accidentally receives them first. 

	*still need to parse recorded sequence into the YAML instead of XML. Right now our test code 	to record sequence are using an f.write function and storing the file as an XML file. Which for obvious reason isn’t working out at all

* recently started working in a logging system but I also need to incorporate handling of trace-back handling for all of our sub-process and os commands that sort of thing.
	- might help to add some hierarchy to this as well but that’s for a later date honestly

*  The GUI was created using GTK and Glade files. A preferences tab has the configuration interface for the user to input the server data and other things. I’m using configure parser to store and pull this information from a stored ini file.

*  The scanner’s interface pulls the scan name from user defined info stored in an ini file that’s used a simple place holder for stored object information. In a nutshell I need a quick and dirty way of storing the file and sequence names so that I could the information from some thing that’s not running.

10-24-2021

**Update the sequence code to run each step perfectly-ish lol.My current code chops up everything into chunks innntervals of (whatever its set to). I can chop it up by commas which I'll have to do soon (unless it breaks the code for some reason then I'll just stick with this.

*** decresed the wait time between each interation taken between each step.  

11-11-2021

* added the abilty to modify GPSdata manually through a gui in prefernces
* ini to make it easy for other users to modify stored gpds data

12-16-2021

*Earlgrey now uses f.write to create a yaml file. I was going to parse the info in but I’m worried about performance issues once the sequences get longer.
*

NEWS 	A basic change-log, intended for users

INSTALL 	Installation instructions
We will get to this once I find some order in everything

COPYING / LICENSE 	Copyright and licensing information
I don’t have any I’m poor that’s why I made this fucking thing

BUGS 	Known bugs and instructions on reporting new ones

* So there's a million this is in the serious beginning stages of prototyping
but here’s a list of my current hurdles:

*** Scanner cuts out a lot when being run from a SBC like a raspberry pi I’m using. I originally designed it to run off I think like 5 Arduino Nano-s. This causes a lot of lost connections and restarts. I think it’s just too much of a voltage draw. So I’ve decided to go with a single Mega 2560 to control all the motors. I made this thing mostly from 3D printer parts and after building, repairing a few of these things I noticed a lot of them run using simple stepper drivers like a1988 (sp?) but yeah common step driver motors some even have a Mega 2560 themselves running things like RepRap (sp?)

*****Any-who my next thing I’m working on CAD-ing out a circuit board to utilize the Mega560  with maybe the embed pi boards I see. I’m going make a hat on the mill soon make some clean connections from the Mega 2560 and the step drivers. Aside from that I think everything I’m designing might have to be sent of to be made cause I simple don’t have the materials here to make this to the specifications that I want.

********Speaking  of CAD (not the same kind but whatever). I need to heavily rework the 3D CAD design for the scanner itself. The tilt function is super wonky and the belt slips a simple work around would be to be a better fitting belt and created a new (whatever I named that part) that allows for better tensions (or allow for tension-ing of the belt). I also want the camera hang so that it can tilt all the way around. I may nix the whole design at that port and replace it with some kind of working gear model but I can’t afford a lot fo the parts for that so for now I’ll cad out some concepts and try to acquire a worthy investor or potential employer. Maybe I’ll make a working model concept with plastic parts. I’m really getting flooded with work on this so we will see. 


*************Need to rework the runscan.py to multithread with a montior progress gui to give the user somethin meaning to look at while they activally scaning an object

******************Solved how to fix the pause issue***********************************

**** The issue is on the Arduino side. We need to make it parse data so that it throws out the next however many characters then do a function “like move motor” then move onto the next until it reaches a marker in the YAML file like “end sequence”

*************** Finally Solved!!!!!*****************************************
It took a lot of tampering and tweaking but I finally found a way to run the sequences from a recorded scan on one line of YAML.
****** I used a recursive function to remove the commas.
****** I then used a replace function to replace the letter r for a return call.
****** After I chunked each interpreted string into sections of 4
****** The re-iterator function is step by the number of characters in one string of the YAML file divided by 3. I did this to allow any number of set steps can be made on a single string without the need to use of unneeded handshaking aside from in the beginning when we test it’s connection for debugging. 


