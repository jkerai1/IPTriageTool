@ECHO OFF
paste > temp.txt
set /p Ip=<temp.txt
SET BROWSER=brave.exe
START %BROWSER% -new-tab "https://www.virustotal.com/gui/ip-address/%Ip%/detection"
exit
