#!/usr/bin/python
#coding=utf-8

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

from handlers.index import IndexHandler
from handlers.down import DownHandler

url = [(r'/', IndexHandler), (r'/down', DownHandler)]
