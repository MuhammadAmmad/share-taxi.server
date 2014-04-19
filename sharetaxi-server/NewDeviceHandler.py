from google.appengine.api import memcache
from google.appengine.ext import ndb
import json
import webapp2




  def post(self):
    dev = Device(id=1,name='lim')
    dev.put()