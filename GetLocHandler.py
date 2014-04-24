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

from google.appengine.ext import ndb
from model_gps_location import Location
from google.appengine.api import urlfetch
from Utils import Utils

class GetLocHandler(webapp2.RequestHandler):
	def get(self):
		#self.response.headers['Content-Type'] = 'text/html'
		#return only active points
		loc_query = Location.query(Location.isActive == True)
		upd_locations = loc_query.fetch()
		locations_json = Utils.items_to_json(upd_locations)
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