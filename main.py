import settings
import script_handler

if __name__ == '__main__':
    # script_handler.run(command=settings.MOBSF_RUN_CMD, path=settings.MOBSF_PATH, shell=True)
    script_handler.run(command=settings.EMULATOR_RUN_CMD, path=settings.EMULATOR_PATH, shell=True)