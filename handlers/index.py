#/usr/bin/python
#coding=utf-8

import tornado.escape
import tornado.web
import os
from conf import upload_path
import json

class IndexHandler(tornado.web.RequestHandler):
  def post(self):
    files = self.request.files["file"]
    for f in files:
      name = f['filename']
      path = os.path.join(upload_path, name)
      with open(path, 'wb') as up:
        up.write(f['body'])
    self.write(json.dumps({'code':0, 'data': 'success', 'msg': 'successful'}))
  
  def get(self):
    self.render('index.html')
