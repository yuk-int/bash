#! /usr/bin/bash

#echo "subnet?"
read -p "subnet:" subnet

if [ -z "$subnet" ]; then
echo "-z is true"

else
echo "searching"
for ip in $(seq 1 254); do ping -c 1 -W 1 $subnet.$ip | grep "ttl"; done
fi
