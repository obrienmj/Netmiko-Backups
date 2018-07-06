# Netmiko-Backups
Python script that utilizes netmiko to backup switches on a network.

***In order to run, you will need to do the following:

1. Install Python 3.6.5 from https://www.python.org/downloads/
    
    -Change installation folder to C:\Python3\
    
2. Install netmiko (instructions are for a Windows Machine):
	
	-Open Command prompt
	
	-Run:  cd C:\Python3\Scripts
	
	-Run:  pip install netmiko
	
3. Create a text file and save it in the Python3 folder.  See Example file.

	-The current script takes device types of hp, extreme or enterasys
	
	-Each line should have the type of device, a space, then the IP address
	
4. Customize to your environment:

	-Change the device password every place you see "P@ssw0rd" in the script, and keep any quotes.
	
	-(Line 30)Enter your TFTP Server where you see 'X.X.X.X', and keep the quotes.  for example:  '1.1.1.1'
	
	-(Line 68-69)Edit email settings to your email account.
	
	-(Line 33)Make sure the file path to the switches.txt file is correct.
