import logging
import os

class LogGen():
    @staticmethod
    def loggen():
        path=os.path.abspath(os.curdir) + '\\logs\\Automation.log'
        logging.basicConfig(filename=path,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m%d%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

