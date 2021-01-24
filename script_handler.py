import subprocess
import shlex
import settings


# https://stackoverflow.com/questions/29633719/subprocess-create-new-console (Check out for windows test)

def run(command, path=settings.BASE_DIR, shell=True):
    cmd = shlex.split(command)
    print(cmd, path, shell)
    if cmd:
        subprocess.Popen(cmd, cwd=path, shell=False)
