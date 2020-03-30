#encoding:utf-8
import logging
import logging
import logging.config


LOG = logging.getLogger(__name__)

logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# temp = raw_input("请输入您的姓名:")
# name = str(temp)
# print "您好" + name
logging.info("haha")
