import os
import os.path
import sys
import getpass

print("wdsdsdf")

## Usage: 
## 	With no argument, will use the current 'calendar' file.
##  use option 'update' to grab a new 'calendar' file.


if( (len(sys.argv)>1) and sys.argv[1] == 'update' ):
	print("You have chosen to update the calendar file.")
	print("Creating a new file, 'calendar.txt' in the following location: "+os.getcwd())
	
	## attempting to grab the data from callendar (ie, do you have internet?)
	os.system('node quickstart.js>attempt.txt')
	filename="attempt.txt"
	file=open(filename, "r")
	if( "getaddrinfo EAI_AGAIN" in file.readline() ):
		print("ERROR: you don't have the internetz.")	

	else:
		os.system('mv attempt.txt calendar.txt')		
		print("Succesfully created new calendar file. Please run again to view changes.")
else:
	filename="calendar.txt"
	file=open(filename, "r")
	print("peeking at first line of file. found")
	text=file.readline()
	error_string="getaddrinfo EAI_AGAIN"
	if( error_string in text):
		print("Your calendar file has an error in it.")
		print("Make sure you're connected to the internet and")
		print("Run this program with the 'update' argument")
		print("Exiting...")
		sys.exit
	else:
		## valid calendar files and internet connection
		username=getpass.getuser()
		print username	


