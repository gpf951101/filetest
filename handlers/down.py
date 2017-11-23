#!/usr/bin/python
#coding=utf-8

import tornado.web
from conf import upload_path
import os

class DownHandler(tornado.web.RequestHandler):
  def get(self):
    filepath = os.path.join(upload_path, 'LICENSE')
    self.set_header('Content-Type', 'application/octet-stream')
    self.set_header('Content-Disposition', 'attachment; filename=LICENSE')
    with open(filepath, 'rb') as f:
      while True:
        data = f.read(1024)
        if not data:
          break;
        self.write(data)
      self.flush()
