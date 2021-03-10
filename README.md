# Upkeepmonitor (UBUNTU)
Student project to monitor network downtime within a network.


### Docker cannot be supported for this program
This project was supposed to be run on Docker, but as docker couldnt access the network devices it was decided that docker cant be used. The docker container cannot access the network which makes the core functionality of the program useless as it could not scan any networks.

### VM cannot be supported for this program
The program can be run on a VM, however when running on a VM nmap will have an issue finding some hosts, therefore running this program on a VM is not encouraged at all.

## Programdescription
This Upkeepmonitor will be scanning your local network and look for any new hosts and if any hosts have been disconnected that have been connected.
It is writing to an sqlite3 database and will log the Hostname,IP,status (Reachable or not reachable),timestamp. It is also writing the same things to an csv file.

The project itself is made to constantly monitor the network and easily have a log if any devices get disconnected. There is also a GUI that will show the status live and it updates every scan.

Sometimes the IP might get marked as "Unknown" since the unit that its trying to look up the ip from might reject the reverse dns lookup, this is normal since some routers or units have a built in protection.

It will prompt you for your network gateway when you start the program and it will then begin to scan the network.


#### This project mainly runs on Ubuntu (confirmed to be working with Ubuntu20.04) however the python code in this repository will run on Windows aswell.

## Installation
Install python with sudo apt-get install python3
install pip with : sudo apt update
			 sudo apt install python3-pip
Make sure following packages are installed, if not install them in the terminal:
python-nmap: pip3 install python-nmap
nmap: sudo apt-get install nmap
Tkinter: sudo apt-get install python-tk
getmac: pip install getmac

### How to run it
First make sure to have all the installed packages, those are listed above in the installation section.
It can easily be run through the terminal:
Right click the folder where the "Upkeepmonitoring" file is downloaded and choose "Open in Terminal"
When in terminal type "sudo ./Upkeepmonitoring"

This will open the prompt for your network gateway, as soon as you enter the gateway the main program will open and run.

To reset the database and/or csv-file, simply remove the file from your directory and it will create a new file when running. 




### Tech stack
* Python for everything.
* Database is sqlite3 (Already built-in python)
* GUI is Tkinter (Also built in Python versions after 3.8)




