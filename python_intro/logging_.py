import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s'
    )

logging.debug("debug msg")
logging.info("info msg")
logging.warning("warning msg")
logging.error("error msg")
logging.critical("critical msg")