import webapp2

from model_cabs_memory import *

class stopDeviceHandler(webapp2.RequestHandler):
	def post(self):
		androidID = self.request.get("androidID")
		for cab in cabs_memory_array:
			if (cab.androidID == androidID):
				cabs_memory_array.remove(cab)