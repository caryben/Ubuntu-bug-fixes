import subprocess
network_name = raw_input("What is the name of your network? ")
subprocess.check_call(['nmcli', 'c', 'up', 'id', network_name])
