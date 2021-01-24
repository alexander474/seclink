import subprocess
import shlex
import settings
import webbrowser
import platform
import os


# https://stackoverflow.com/questions/29633719/subprocess-create-new-console (Check out for windows test)

def run(command, path=settings.BASE_DIR, shell=True):
    cmd = command
    process = None
    print("CMD: ", cmd)
    print("PATH: ", path)
    if cmd:
        # DETACHED_PROCESS flag to open separate terminal | preexec_fn=os.setpgrp for Linux
        if platform.system() == settings.LINUX:
            process = subprocess.run(cmd, cwd=path, shell=shell, preexec_fn=os.setpgrp)
        elif platform.system() == settings.WINDOWS:
            process = subprocess.run(cmd, cwd=path, shell=shell, creationflags=subprocess.DETACHED_PROCESS)
        print("ARGS: ", process.args)
    return process


def popen(command, path=settings.BASE_DIR, shell=True):
    cmd = command
    process = None
    print("CMD: ", cmd)
    print("PATH: ", path)
    if cmd:
        # DETACHED_PROCESS flag to open separate terminal | preexec_fn=os.setpgrp for Linux
        if platform.system() == settings.LINUX:
            process = subprocess.Popen(cmd, cwd=path, shell=shell, preexec_fn=os.setpgrp)
        elif platform.system() == settings.WINDOWS:
            process = subprocess.Popen(cmd, cwd=path, shell=shell, creationflags=subprocess.DETACHED_PROCESS)
        print("ARGS: ", process.args)
        # Opens in browser
        webbrowser.open(f"http://{settings.MOBSF_IP}:{settings.MOBSF_PORT}", autoraise=True)
    return process
