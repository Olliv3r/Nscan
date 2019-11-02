#!/usr/bin/env bash
clear
tput cup 0
tput civis
echo -e "\r\033[0mInstalling...[\033[01;93mNone\033[0m]"
(apt update && apt upgrade -y && apt install nmap python -y && pip  install python-nmap) &> /dev/null
tput cup 0
echo -e "\r\033[0mInstalling...[\033[01;93mDone\033[0m]"

echo -e "\033[01;92mpython3 ./Nscan py"
tput cnorm
