import settings
import script_handler

if __name__ == '__main__':
    print(settings.BASE_DIR)
    script_handler.run(command=settings.MOBSF_RUN_CMD, path=settings.MOBSF_PATH, shell=True)