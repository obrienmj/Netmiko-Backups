from netmiko import ConnectHandler
import smtplib

#Define functions for each Device Type
def netmiko_exos(ip):
    return{
	'device_type': 'extreme',
	'ip': ip,
	'username': 'admin',
	'password': 'NOT2ez2guess',
	}
	
def netmiko_enterasys(ip):
    return{
	'device_type': 'enterasys',
	'ip': ip,
	'username': 'admin',
	'password': 'NOT2ez2guess',
	}
	
def netmiko_hp(ip):
    return{
	'device_type': 'hp_procurve',
	'ip': ip,
	'username': 'manager',
	'password': 'NOT2ez2guess',
	}	

#Specify TFTP Server
tftpServer = '10.20.4.20'

#Open Text file with IP address per line
addrFile = open(r'C:\Scripts\switches.txt','r')

#create a list called linelist for each line in the file.  The first item is the device type, the second item is the IP address
for line in addrFile:
    linelist = line.split()
    ipADDR = linelist[1]

    #Check the first item of the list to determine device type and set variables
    if linelist[0] == 'extreme':
        HOST = netmiko_exos(ipADDR)
        saveConfig = 'save config' + '\ny\n'
        CopyFile = 'tftp put ' + tftpServer + ' vr "VR-Default" primary.cfg' + ' ' + ipADDR + '.cfg'
    elif linelist[0] == 'hp':
        HOST = netmiko_hp(ipADDR)
        saveConfig = 'write memory'
        CopyFile =  'copy running-config tftp ' + tftpServer + ' ' + ipADDR + '.cfg'
    elif linelist[0] == 'enterasys':
        HOST = netmiko_enterasys(ipADDR)
        saveConfig = 'show config outfile configs/current.cfg' + '\ny\n'
        CopyFile = 'copy configs/current.cfg tftp://' + tftpServer + '/' + ipADDR + '.cfg'
    elif linelist[0] == 's3':
        HOST = netmiko_enterasys(ipADDR)
        saveConfig = 'show config outfile slot1/current.cfg' + '\ny\n'
        CopyFile = 'copy slot1/current.cfg tftp://' + tftpServer + '/' + ipADDR + '.cfg'
    else:
        print("The device type is either not in the text file or incorrect.  See ReadMe.txt")
        break

    #Run SSH commands on switch
    net_connect = ConnectHandler(**HOST)
    net_connect.send_command(saveConfig)
    net_connect.send_command(CopyFile)
    net_connect.disconnect()

addrFile.close()


#Configure email
gmail = smtplib.SMTP_SSL('smtp.gmail.com', 465)
gmail.login('ltech@rockyhillps.com', 'NOT2ez2guess')
gmail.sendmail('ltech@rockyhillps.com', 'netadmin@rockyhillps.com', 'Subject: Switch Backups Completed\n\nThe script to backup all switch configurations has been completed.\nPlease view the files on WSUS01 in C:\TFTP-Root')
gmail.quit()
