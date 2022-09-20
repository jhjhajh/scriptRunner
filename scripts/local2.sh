#!/bin/bash

echo "client machine"

#ssh -i "carbanaktest2.pem" kali@ec2-35-171-225-42.compute-1.amazonaws.com 
#'bash -s' << 'ENDSSH'
 # echo "test"
 # cd /home/
 pwd
#ENDSSH
echo "connecting to client machine..."
sshpass -p kali ssh -t kali@10.0.2.15 << 'ENDSSH'
  echo "connected to client"
  cd /home/kali/Desktop
  ./payload.bin
  echo "payload executed"
ENDSSH


