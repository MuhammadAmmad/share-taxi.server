import jinja2
import os
import webapp2
import sys
import string
import traceback
import cgi

from google.appengine.ext import ndb
from model_gps_location import Location
from google.appengine.api import urlfetch

jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))



class showLocations(webapp2.RequestHandler):

# loc = Location(longitude=-122.084095,latitude=37.422006)
# dev = Device(id=1,name-'lim',curr_location=loc)
# dev.put()

  def get(self):
    #insDevice()
    self.response.headers['Content-Type'] = 'text/html'
    Location_query = Location.query()
    locs = Location_query.fetch(10)
    for l in locs:
        self.response.write('<b>%s</b>\n' % l.latitude)
        self.response.write('<b>%s</b>\n' % l.longitude)
        #self.response.write('<b>%s</b>\n\n' % l.date)

    #self.response.write('<b>%s</b>' % devices.name)
