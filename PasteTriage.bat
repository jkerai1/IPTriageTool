@ECHO OFF
paste > temp.txt ###need paste installed see https://www.c3scripts.com/tutorials/msdos/paste.html
set /p Ip=<temp.txt
SET BROWSER=brave.exe
START %BROWSER% -new-tab "https://www.virustotal.com/gui/ip-address/%Ip%/detection"
exit
