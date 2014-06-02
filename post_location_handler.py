import webapp2
import datetime

from model_cabs_memory import *

class PostLocHandler(webapp2.RequestHandler):
  def post(self):
    curr_date = datetime.datetime.now()
    androidIDStr = self.request.get("androidID")
    longStr = self.request.get("longitude")
    latStr = self.request.get("latitude")
    for cab in cabs_memory_array:
        if (cab.androidID == androidIDStr):
            if (cab.date < curr_date):
                cab.update_cab(curr_date, longStr, latStr)