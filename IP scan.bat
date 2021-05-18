@echo off

SET BROWSER=firefox.exe
SET /p Ip= What is IP? 

START %BROWSER% -new-tab "https://www.virustotal.com/gui/ip-address/%Ip%/detection"
START %BROWSER% -new-tab "https://otx.alienvault.com/indicator/ip/%Ip%"
START %BROWSER% -new-tab "https://who.is/whois-ip/ip-address/%Ip%"