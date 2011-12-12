import logging
from py_generic_utils import handlers

logger = logging.getLogger()

h = handlers.TimedRotatingFileHandler('my_file.log', when='midnight')

logger.addHandler(h)

logger.error('first message')
h.doRollover()
logger.error('second message')
