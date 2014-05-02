
from google.appengine.api import memcache
import json
import webapp2

# from feed_handler import FeedHandler
# from model_choosie_post import ChoosiePost
# from utils import Utils
#from model_device import insDevice()
#from model_device import searchDevice()
#from model_gps_location import Location

import jinja2
import os
import traceback

jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))



class HomepageHandler(webapp2.RequestHandler):
# loc = Location(longitude=-122.084095,latitude=37.422006)
# dev = Device(id=1,name-'lim',curr_location=loc)
# dev.put()
    # def post(self):
    #     curr_location = Location(longitude="0.1",latitude="0.2",androidID="3",lineNum="4",direction="N")
    #     curr_location.put()
  # def get(self):
  #   #insDevice()
  #   self.response.headers['Content-Type'] = 'text/html'
  #   devices = searchDevice(1)
  #   for d in devices:
  #       self.response.write('<b>%s</b>' % d.name)
    #self.response.write('<b>%s</b>' % devices.name)


    def get(self):
      self.response.headers['Content-Type'] = 'text/html'
      template = jinja_environment.get_template('index.html')
      self.response.write(template.render())