#!/usr/bin/env bash

apt update
apt upgrade
apt install nmap python
pip install python-nmap

if test -d /usr/bin;then
	cat Nscan.py >> /usr/bin/Nscan
	chmod 777 /usr/bin/Nscan
elif test -d $PREFIX/bin;then
	cat Nscan.py >> $PREFIX/bin/Nscan
	sleep 0.5
	echo "Run 'Nscan'"
fi
