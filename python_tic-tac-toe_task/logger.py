"""module for init_ logger"""
import logging
# import logging.config
# import yaml
#
#
# with open('config.yaml', 'r') as f:
#     config = yaml.safe_load(f.read())
#     logging.config.dictConfig(config)
#
# log_ = logging.getLogger('log_')


# logging.basicConfig(filename='ttt.txt', filemode='a', format='[%(asctime)s] %(message)s')
# logging.basicConfig(format='[%(asctime)s] %(message)s')

log_ = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('ttt.txt')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.WARNING)

# Create formatters and add it to handlers
c_format = logging.Formatter('[%(asctime)s] %(message)s')
f_format = logging.Formatter('[%(asctime)s] %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

log_.addHandler(c_handler)
log_.addHandler(f_handler)
