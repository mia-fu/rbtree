#!/usr/local/bin/python
# -*- coding:utf-8 -*-
import logging
import logging.config

logging.config.fileConfig('logginf.cnf')

logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')