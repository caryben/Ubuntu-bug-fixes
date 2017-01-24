# this just resets the wifi symbol at the top of the screen if it's not working properly. Sometimes when I start up Ubuntu on 
# my laptop it doesn't appear at all so this corrects that instead of me having to restart my computer.

import subprocess, sys
subprocess.check_call(['killall', 'nm-applet'])
subprocess.check_call(['setsid', 'nm-applet'])
