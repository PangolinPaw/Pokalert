try:
	import outlook # Windows
except:
	import gmail # Linux
import pgoHeatmap
import os

def getAlertList():
	alertFile = open("alertList.txt", "r")
	alertList = alertFile.readlines()
	numList = []
	for num in alertList:
		numList.append( int(num.rstrip()) )
	alertFile.close()
	return numList

def loadSettings():
    # Load default settinsg from settings.txt if no arguments are provided on program start
    settingFile = open("settings.txt", "r")
    settings = settingFile.readlines()

    username, password, location = "", "", ""
    for item in settings:
        item = item.split("=")
        if item[0] == "username":
            username = item[1].strip()
        elif item[0] == "password":
            password = item[1].strip()
        elif item[0] == "location":
            location = item[1]
        elif item[0] == "email":
            emailAlerts = item[1]
        elif item[0] == "gmail":
            gmailAcc = item[1]
        elif item[0] == "gmailPassword":
            gmailPass = item[1]
        else:
            print " [!] Error: Unrecognised setting '{0}' in settings.txt.".format(item[0])

    return emailAlerts, gmailAcc, gmailPass

def alert(num, name, lat, lon, expiresAt):
	"Send a notification if a pokemon on the 'interestring' list appears"
	if num in getAlertList():
		mapfile = pgoHeatmap.makeMap(lat, lon, name)
		mapfile = "{0}\\{1}".format(os.path.dirname(os.path.realpath(__file__)), mapfile)
		message =  """ 
A wild {0} appeared!
Location: \t https://www.google.com/maps?q={1},{2}
Expires at:\t{3}""".format(name, lat, lon, expiresAt)
		print "Sending {0}".format(mapfile)

		emailAlerts, gmailAcc, gmailPass = loadSettings()

		try:
			outlook.sendMessage(emailAlerts, "PKMN", message, mapfile) # WINDOWS
		except:
			gmail.attach(gmailAcc, gmailPass, emailAlerts, "PKMN", message, mapfile)# LINUX



