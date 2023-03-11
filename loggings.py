
import logging

# create and configure logger

logging.basicConfig(filename="CT10.log", format='%(asctime)s %(message)s', filemode='w')
logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

logger.error("Your error message!")
logger.critical("Your critical message!")
logger.debug("Your debug message!")
logger.info("Your info message!")
logger.warning("Your warning message!")