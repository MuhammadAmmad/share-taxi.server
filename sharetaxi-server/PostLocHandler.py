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

class PostLocHandler(webapp2.RequestHandler):
  def post(self):
    # get param from url
    longStr = self.request.get("longitude")
    latStr = self.request.get("latitude")
    androidIDStr = self.request.get("androidID")
    lineNumStr = self.request.get("lineNum")
    directionStr = self.request.get("direction")

    # store in ndb:
    if longStr:
      # check if exist
      qry= Location.query(Location.androidID == androidIDStr).get()
      #exist (update):
      if qry:
        qry.longitude = longStr
        qry.latitude = latStr
        qry.lineNum = lineNumStr
        qry.direction = directionStr
        qry.isActive = True
        qry.put()

      # doesn't exist (insert):  
      else:
        curr_location = Location(longitude = longStr,
                  latitude = latStr, androidID = androidIDStr
                  ,lineNum=lineNumStr,direction=directionStr,isActive=True)
        curr_location.put()