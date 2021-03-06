import logging


# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s - %(levelname)s - %(message)s",
#     filename='server.log'
# )

def setup_logging():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(name)s---%(asctime)s - %(levelname)s - %(message)s')
    fh = logging.FileHandler('log_dir/ser.log')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger


logger = setup_logging()
