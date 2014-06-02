import webapp2

from model_cabs_memory import *

class updCabOccupation(webapp2.RequestHandler):
   def post(self):
	androidIDStr = self.request.get("deviceID")
	freeSeats = self.request.get("freeSeats")
	for cab in cabs_memory_array:
		if (cab.androidID == androidIDStr):
			cab.update_freeSeats(freeSeats)