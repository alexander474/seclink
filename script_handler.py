import subprocess
import shlex
import settings
import webbrowser


# https://stackoverflow.com/questions/29633719/subprocess-create-new-console (Check out for windows test)

def run(command, path=settings.BASE_DIR, shell=True):
    cmd = command  # shlex.split(command)
    print("CMD: ", cmd)
    print("PATH: ", path)
    if cmd:
        # DETACHED_PROCESS flag to open separate terminal
        process = subprocess.run(cmd, cwd=path, shell=shell, creationflags=subprocess.DETACHED_PROCESS)
        print("ARGS: ", process.args)
        

def popen(command, path=settings.BASE_DIR, shell=True):
    cmd = command  # shlex.split(command)
    print("CMD: ", cmd)
    print("PATH: ", path)
    if cmd:
        # DETACHED_PROCESS flag to open separate terminal
        process = subprocess.Popen(cmd, cwd=path, shell=shell, creationflags=subprocess.DETACHED_PROCESS)
        print("ARGS: ", process.args)
        # Opens webbrowser
        webbrowser.open(f"http://{settings.MOBSF_IP}:{settings.MOBSF_PORT}", autoraise=True)

#def open_browser(ip, port):
    #print(ip, port)
    #webbrowser.open(f"http://{ip}:{port}", autoraise=True)
