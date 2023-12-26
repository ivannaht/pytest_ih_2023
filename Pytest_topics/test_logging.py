import logging


def test_logging():
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler("logfile.log")
    formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    logger.debug("logger.debug")
    logger.info("logger.info")
    logger.warning("logger.warning")
    logger.error("logger.error")
    logger.critical("logger.critical")
