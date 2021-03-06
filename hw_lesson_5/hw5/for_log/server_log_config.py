import logging

logger = logging.getLogger('app2.main')
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s  = %(lineno)d")
fh = logging.FileHandler("logs/app2.main.log", encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)
if __name__ == '__main__':
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logger.addHandler(console)
    logger.debug('Тестовый запуск логирования server')
