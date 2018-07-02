""" Settings added as specified in following link
http://docs.gunicorn.org/en/stable/settings.html
"""

import multiprocessing
from instance import config as conf


bind = '{}:{}'.format(conf.HOST, conf.PORT)
workers = (multiprocessing.cpu_count() * 2) + 1
