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

from google.appengine.ext import ndb
from model_gps_location import Location
from google.appengine.api import urlfetch

class GetLocHandler(webapp2.RequestHandler):
	def get(self):
		#self.response.headers['Content-Type'] = 'text/html'
		# give only active points
		loc_query = Location.query(Location.isActive == True)
		upd_locations = loc_query.fetch()
		for loc in upd_locations:
			self.response.headers['Content-Type'] = 'text/html'
			self.response.write(json.dumps(loc.to_json()))