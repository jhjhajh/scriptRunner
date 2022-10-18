import paramiko

## to start winlogbeat 
start_beat = "net start winlogbeat"
## config to auto start
auto_beat = "sc config winlogbeat start=auto"
## to stop winlogbeat
stop_beat = "net stop winlogbeat"

def init_connection(host='192.168.147.206', user='victim-1', password='123', port=22):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(host, port, user, password)
	return ssh 

def run_command(ssh, command):
	stdin, stdout, stderr = ssh.exec_command(command)
	lines = stdout.readlines()
	return lines
	
ssh = init_connection()
lines = run_command(ssh, "powershell.exe -ExecutionPolicy bypass .\\webreq.ps1")

print(lines)
