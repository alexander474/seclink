import subprocess
import shlex
import settings


# https://stackoverflow.com/questions/29633719/subprocess-create-new-console (Check out for windows test)

def run(command, path=settings.BASE_DIR, shell=True):
    cmd = command  # shlex.split(command)
    print("CMD: ", cmd)
    print("PATH: ", path)
    if cmd:
        process = subprocess.Popen(cmd, cwd=path, shell=shell)
        print("ARGS: ", process.args)
