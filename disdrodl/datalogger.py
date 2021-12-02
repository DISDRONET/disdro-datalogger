import time
import logging
from .parsivel import Parsivel
from .thies import Thies

logger = logging.getLogger('disdrometer_logger')
logger.setLevel(logging.INFO)


class ParsivelDataLogger(Parsivel):
    def __init__(self):
        super().__init__()
