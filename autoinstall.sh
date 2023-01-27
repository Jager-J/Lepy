#!/bin/sh
sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get tree -y && sudo apt-get clamscan -y
clear
echo "Updates Installed & Added ClamScan antivirus & tree"
sudo mkdir /USB
sudo mkdir /USB/{1..4}

echo "/dev/sda1 /USB/1 vfat defaults 0 1"
echo "/dev/sdb1 /USB/2 vfat defaults 0 1"
echo "/dev/sdc1 /USB/3 vfat defaults 0 1"
echo "/dev/sdd1 /USB/4 vfat defaults 0 1"
