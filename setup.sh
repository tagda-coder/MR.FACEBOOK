#!/usr/bin/bash 
clear
echo
echo -e "\033[32m\033[1mInstalling Required Packages" | pv -qL 10 
echo -e "\033[33m---------------------------------\033[0m"
apt update -y
apt upgrade -y

pkg install python -y

pip install requests
pip install re 


echo -e "\033[32m\033[1mProgram Launching...." | pv -qL 10

rm setup.sh 

python main.py

 
