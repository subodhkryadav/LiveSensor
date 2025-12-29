from sensor.exception import sensorException
from sensor.logger import logging

import os
import sys

def test_exception():
    try:
        a=1/0
    except Exception as e:
        raise sensorException(e,sys)
    

if __name__=="__main__":
    try:
        logging.info("error handle")
        test_exception()   
    except Exception as e:
        print(e)