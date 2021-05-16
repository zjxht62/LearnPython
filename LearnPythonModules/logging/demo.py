import logging
default_logger = logging.getLogger('parent')
default_logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)20s - %(levelname)8s - %(message)s')
# 创建一个用于console的handler，设置级别为INFO
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
default_logger.addHandler(ch)

child_logger = logging.getLogger('parent.child')
fh = logging.FileHandler('aaa.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
child_logger.addHandler(fh)

child_logger.debug('a debug log')
child_logger.info('a info log')
child_logger.warning('a warning log')
child_logger.error('a error log')
child_logger.critical('a critical log')
