import json
import webapp2
import cgi
import urllib
import urllib2
import jinja2
import os
import sys
import string
import traceback

from google.appengine.ext import ndb
from model_gps_location import Location
from google.appengine.api import urlfetch

#from google.appengine.ext import webapp

#jinja_environment = jinja2.Environment(
 #   loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

class stopDeviceHandler(webapp2.RequestHandler):
  def post(self):
    # get param from url
    androidIDStr = self.request.get("androidID")
    # check if exist
    qry= Location.query(Location.androidID == androidIDStr).get()
    #exist (update):
    if qry:
      qry.longitude = "0.0"
      qry.latitude = "0.0"
      qry.isActive = False
      qry.put()