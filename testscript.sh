#!/bin/bash

echo "connecting to c2 server..."

ssh -i "carbanaktest2.pem" kali@ec2-35-171-225-42.compute-1.amazonaws.com 'bash -s' << 'ENDSSH'
  echo "connected to c2 server"
  
# tmux
# start metasploit listener
# switch tab
# listen on the tab
ENDSSH
