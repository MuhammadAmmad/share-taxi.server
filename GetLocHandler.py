import sys
import string
import traceback
import cgi
import webapp2
import urllib
import urllib2
import jinja2
import os
import json
from collections import OrderedDict

#from google.appengine.ext import ndb
from startDeviceHandler import Location
from startDeviceHandler import startDeviceHandler
#from startDeviceHandler import curr_location
from startDeviceHandler import *
from google.appengine.api import urlfetch
from Utils import Utils

class GetLocHandler(webapp2.RequestHandler):
	def get(self):
		#self.response.headers['Content-Type'] = 'text/html'
		#return only active points
		#loc_query = Location.query(Location.isActive == True)
		#startDeviceHandler.curr_location
		upd_locations = startDeviceHandler.curr_location
		#upd_locations = loc_query.fetch()
		locations_json = upd_locations.to_json()
		#for loc in upd_locations:
		self.response.headers['Content-Type'] = 'text/html'
			#jsonStr = loc.to_json()
		self.response.write(json.dumps({'points': locations_json}, sort_keys=False))
#for tests:
		# result = OrderedDict([
  #               ("androidID","test2"),
  #               ("date","test2"),
  #               ("lineNum","test3"),
  #               ("direction","test4"),
  #   			("longitude","test5"),
  #   			("latitude","test6")
  #   			])
		# self.response.headers['Content-Type'] = 'text/html'
		# self.response.write(json.dumps(result, sort_keys=False,ensure_ascii=False))