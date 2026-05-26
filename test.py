import numpy as np
import logging

logging.basicConfig(filename= 'mmmmm.log,
                      format= '%(asctime)s %(message)s',
                      level= logging.INFO,
                      filemode= 'w')
  
logger_test = logging.getLogger("test") 

logger_test.info(f'asdadsadasdadsasdasd')
