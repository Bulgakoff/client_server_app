import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s ",
    filename='log_dir/user.log'
)

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
#
# formatter = logging.Formatter('%(name)s---%(asctime)s - %(levelname)s - %(message)s')
# fh = logging.FileHandler('log_dir/ser_cl.log')
# fh.setFormatter(formatter)
# logger.addHandler(fh)