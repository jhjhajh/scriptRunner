#!/bin/bash
# username of server
user="apt" 
# ip address of server
ip="192.168.147.225"

echo "Connecting to server..."

# virsh
ssh -tt "${user}@${ip}" 'bash -s'<< SSH
    virsh snapshot-revert --domain win10-clone --snapshotname "demo"
    virsh reboot --domain win10-clone
SSH

echo "Instances started, ready to begin simulation"
