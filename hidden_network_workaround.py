# My computer was failing to recognize wifi networks after being woken up from sleep so this uses the network manager command
# line tool to force my computer to recognize the network I type in to the terminal.

import subprocess
network_name = raw_input("What is the name of your network? ")
subprocess.check_call(['nmcli', 'c', 'up', 'id', network_name])
