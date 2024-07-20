#! /usr/bin/bash
# Name: ipSearch.sh
# Purpose: find local ip 
# Author:
# -------------------------------------------------------

#echo "subnet?"

ifconfig -a
ifconfig | grep inet | grep -v '127.0.0.1' | cut -d: -f2 | awk '{print $2}'

read -p "subnet:" subnet

if [ -z "$subnet" ]; then
echo "-z $subnet is true"

else
echo "searching $subnet .1 to .254"
for ip in $(seq 1 254); do ping -c 1 -W 1 $subnet.$ip | grep "ttl"; done
fi
