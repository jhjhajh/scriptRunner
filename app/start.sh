#!/bin/bash
user="apt"
ip="192.168.147.225"

echo "Connecting to server..."

ssh -tt "${user}@${ip}" 'bash -s'<< SSH
    virsh snapshot-revert --domain win10-clone --snapshotname "revertTest"
    virsh reboot --domain win10-clone
SSH

echo "Instances started, ready to begin simulation"
