import webbrowser
import re #Regex
import sys

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

def CheckIP(Ip):
    if(re.search(regex, Ip)):
        pass ##no need to do anything if IP is valid
    else:
        sys.exit() ##This is a cop-out but oh well

        
Num = int(input("how many IP address? "))
IPList = []
counter = 0


while counter != Num:    
    print("\n" + str(counter + 1) + ":")
    
    IP_Temp = (input("IP address: ?  ")) #Get Input and sanitize it
    IP_Temp = IP_Temp.replace("-", "")
    IP_Temp = IP_Temp.replace(" ","")
    
    CheckIP(IP_Temp)
    IPList.append(IP_Temp)
    counter += 1
    
    
for ele in IPList: 

    webbrowser.open("https://www.virustotal.com/gui/ip-address/" + ele+ "/detection")
    webbrowser.open("https://who.is/whois-ip/ip-address/" + ele)
    webbrowser.open("https://otx.alienvault.com/indicator/ip/" + ele)
