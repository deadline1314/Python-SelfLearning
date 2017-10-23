# from shell to script
import subprocess


subprocess.call('dir', shell=True)
subprocess.call('ls', shell=True)


output = subprocess.call('dir', shell=True)
print(output)
