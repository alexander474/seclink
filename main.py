import settings
import script_handler

if __name__ == '__main__':
    # MobSF Popen command
    script_handler.popen(command=settings.MOBSF_RUN_CMD, path=settings.MOBSF_PATH, shell=True)
    # Emulator run command
    script_handler.run(command=settings.EMULATOR_RUN_CMD, path=settings.EMULATOR_PATH, shell=True)