import subprocess
import settings
import webbrowser
import os


# https://stackoverflow.com/questions/29633719/subprocess-create-new-console (Check out for windows test)

def run(command=None, path=None, shell=True):
    cmd = command
    process = None
    print("CMD: ", cmd)
    print("PATH: ", path)
    if cmd and path:
        # DETACHED_PROCESS flag to open separate terminal | preexec_fn=os.setpgrp for Linux
        if settings.IS_LINUX:
            process = subprocess.run(cmd, cwd=path, shell=shell, preexec_fn=os.setpgrp)
        elif settings.IS_WINDOWS:
            process = subprocess.run(cmd, cwd=path, shell=shell, creationflags=subprocess.DETACHED_PROCESS)
        print("ARGS: ", process.args)
    return process


def popen(command=None, path=None, shell=True):
    cmd = command
    process = None
    print("CMD: ", cmd)
    print("PATH: ", path)
    if cmd and path:
        # DETACHED_PROCESS flag to open separate terminal | preexec_fn=os.setpgrp for Linux
        if settings.IS_LINUX:
            process = subprocess.Popen(cmd, cwd=path, shell=shell, preexec_fn=os.setpgrp)
        elif settings.IS_WINDOWS:
            process = subprocess.Popen(cmd, cwd=path, shell=shell, creationflags=subprocess.DETACHED_PROCESS)
        print("ARGS: ", process.args)
        # Opens in browser
        webbrowser.open(f"http://{settings.MOBSF_IP}:{settings.MOBSF_PORT}", autoraise=True)
    return process
