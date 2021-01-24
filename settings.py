import platform
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# OS VARIABLES
CURRENT_OS = platform.system()
WINDOWS = "Windows"
LINUX = "Linux"
OSX = "Darwin"
IS_WINDOWS = CURRENT_OS == WINDOWS
IS_LINUX = CURRENT_OS == LINUX
IS_OSX = CURRENT_OS == OSX

# MobSF VARIABLES
MOBSF_PATH = "/home/blacktype/Documents/private/tools/Mobile-Security-Framework-MobSF"
MOBSF_IP = "127.0.0.1"
MOBSF_PORT = "8000"
MOBSF_RUN_FILE = "./run.sh"
MOBSF_RUN_CMD = f"{MOBSF_RUN_FILE} {MOBSF_IP}:{MOBSF_PORT}"

# EMULATOR VARIABLES
EMULATOR_PATH = "/home/blacktype/Android/Sdk/emulator"
EMULATOR_AVD_NAME = "Nexus_6_API_28"
EMULATOR_RUN_FILE = "./emulator"
EMULATOR_RUN_CMD = f"{EMULATOR_RUN_FILE} -avd {EMULATOR_AVD_NAME} -writable-system -no-snapshot"
