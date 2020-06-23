import logging
"""
logging.basicConfig(filename="__name__"+".txt", level=logging.INFO,
					format='%(levelname)s:%(name)s:%(message)s')
Sets up the logging for different module.
"""

logger=logging.getlogger(__name__)  #set the logger for this module
logger.setlevel(logging.INFO)


logfile_handle = logging.FileHandler(module_name+'.log')
logger.addHandler(logfile_handle)

logfile_formatter=logging.Formatter('%(levelname)s:%(name)s:%(message)s')
lofile_handle.setFormatter(logfile_formatter)

stream_handler=logging.StreamHandler(stdout)
logger.addHandler(stream_handler)

def main(*args, **kwargs):
	for arg in args:
		

if __name__ == '__main__':
	main()