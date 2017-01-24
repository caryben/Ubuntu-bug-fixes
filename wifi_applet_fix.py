import subprocess, sys
subprocess.check_call(['killall', 'nm-applet'])
subprocess.check_call(['setsid', 'nm-applet'])
