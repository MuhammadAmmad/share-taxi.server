import webapp2
import json

from model_cabs_memory import *
from Utils import *

class GetLocHandler(webapp2.RequestHandler):
	def get(self):
		json_arr = Utils.items_to_json(cabs_memory_array)
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write(json.dumps({'points': json_arr}, sort_keys=False))