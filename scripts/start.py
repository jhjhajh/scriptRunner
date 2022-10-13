#!/usr/bin/env python3
import subprocess

subprocess.Popen(f"ssh kali@192.168.64.2", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

# -----------------------------------------------
# start ssh
# ssh apt@192.168.147.225
# virsh snapshot-revert --domain win10-clone --snapshotname "revertTest"
# virsh reboot --domain win10-clone

# exit ssh

# no output
# results = run_ssh_cmd('my_remote_host.com', 'ls -l').stdout.read()
# print(results)

# for output
# 
