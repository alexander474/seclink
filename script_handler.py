import subprocess
import platform
import settings
import os
import shlex


# https://stackoverflow.com/questions/29633719/subprocess-create-new-console (Check out for windows test)

def run(command=[]):
    cmd = shlex.split(create_command(command))
    print(cmd)
    if cmd:
        # subprocess.call(cmd)
        # os.system("gnome-terminal -e 'echo hey'")
        subprocess.Popen(cmd, shell=True)
        #subprocess.Popen('echo $HOME', shell=True)


def create_command(command):
    current_os = platform.system()
    switcher = {
        settings.LINUX: settings.LINUX_TERMINAL,
        settings.WINDOWS: settings.WINDOWS_TERMINAL,
        settings.MAC: settings.LINUX_TERMINAL,
    }
    return switcher.get(current_os, None)
