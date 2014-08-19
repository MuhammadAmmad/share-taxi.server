import webapp2
import datetime

from model_cabs_memory import *
  
class startDeviceHandler(webapp2.RequestHandler):
  def post(self):
    androidIDStr = self.request.get("androidID")
    curr_date = datetime.datetime.now()
    lineNum = self.request.get("lineNum")
    longitude = self.request.get("longitude")
    latitude = self.request.get("latitude")

    cab_not_in_array = True
    for cab in cabs_memory_array:
        if (cab.androidID == androidIDStr):
            cab_not_in_array = False
            if (cab.date < curr_date):
                cab.update_cab(curr_date, longitude, latitude)

    if (cab_not_in_array):
        new_cab = cabObject(androidIDStr,curr_date,lineNum,longitude,latitude)
        cabs_memory_array.append(new_cab)