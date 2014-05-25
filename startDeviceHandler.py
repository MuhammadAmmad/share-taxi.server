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
import traceback
import cgi
import sys
import string
import traceback
from collections import OrderedDict
import time
import datetime

#from google.appengine.ext import ndb
#from model_gps_location import Location
from google.appengine.api import urlfetch
from google.appengine.ext import webapp

#jinja_environment = jinja2.Environment(
 #   loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

#class globalVar(object):
  

class Location(object):
    longitude = "34.7779045"
    latitude = "32.0590423"
    date = ""
    androidID = "1234"
    lineNum = "4"
    #direction = ndb.StringProperty(required= True,choices=['N','S'])
    isActive = "False"

    def _init_():
      self.longitude = "34.7779045"
      self.latitude = "32.0590423"
      self.date = ""
      self.androidID = "1234"
      self.lineNum = "7"
      #direction = ndb.StringProperty(required= True,choices=['N','S'])
      self.isActive = "False"

    def to_json(self):
  #dateStr = lambda: int(round(self.date.time() * 1000))
  #dateStr = self.date.strftime('%Y-%m-%d @ %H:%M:%S')
      timeVar = datetime.datetime.now()
      timeUnix = time.mktime(timeVar.timetuple())
      result = OrderedDict([
            ("androidID",self.androidID),
            ("date",timeUnix),
            ("lineNum",self.lineNum),
            #("direction",self.direction),
      ("longitude",self.longitude),
      ("latitude",self.latitude)
      ])
      return result

class startDeviceHandler(webapp2.RequestHandler):
  global curr_location
  curr_location = Location()
  def post(self):
    #curr_location = Location()
    # get param from url
    #global curr_location
    curr_location.longitude = self.request.get("longitude")
    curr_location.latitude = self.request.get("latitude")
    curr_location.androidID = self.request.get("androidID")
    #global curr_location
    #curr_location. = self.request.get("lineNum")
    #directionStr = self.request.get("direction")
    # store in ndb:
    #if longStr:
      # check if exist
   #qry= Location.query(Location.androidID == androidIDStr).get()
      #exist (update):
    # if qry:
    #   qry.longitude = longStr
    #   qry.latitude = latStr
    #   qry.lineNum = lineNumStr
    #   #qry.direction = directionStr
    #   qry.isActive = True
    #   qry.put()
    #   # doesn't exist (insert):  
    # else:
    #   curr_location = Location(longitude = longStr,
    #             latitude = latStr, androidID = androidIDStr
    #             ,lineNum=lineNumStr,isActive=True)
    #   curr_location.put()