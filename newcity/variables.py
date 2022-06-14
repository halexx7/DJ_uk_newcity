import os


# Кодировка проекта
ENCODING = "utf-8"

# Ключи используемые в протоколе логирования
ROOT = os.getcwd()
DIR_LOG = "logs"

LOG_DIRECTORY = os.path.join(ROOT, DIR_LOG)
LOG_FILENAME = os.path.join(LOG_DIRECTORY, "app.log")

LOGGER_NAME = __name__

WHEN_INTERVAL = "D"

# Красивости
INDENT = 30 * "-"