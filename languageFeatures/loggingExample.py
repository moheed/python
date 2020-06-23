import logging
"""
logging.basicConfig(filename="__name__"+".txt", level=logging.INFO,
					format='%(levelname)s:%(name)s:%(message)s')
"""

logger=logging.getlogger(__name__)  #set the logger for this module
logger.setlevel(logging.INFO)


logfile_handle = logging.FileHandler('employee.log')
logger.addHandler(logfile_handle)

logfile_formatter=logging.Formatter('%(levelname)s:%(name)s:%(message)s')
lofile_handle.setFormatter(logfile_formatter)

stream_handler=logging.StreamHandler()
logger.addHandler(stream_handler)


