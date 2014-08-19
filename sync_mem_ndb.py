import datetime
import webapp2

from google.appengine.ext import ndb
from model_cabs_memory import *
from model_cabs_ndb import *
from Utils import *

class syncMemNdb(webapp2.RequestHandler):
	def get(self):
		
		update_cabs_array = []
		# read from NDB:	
		array_from_ndb = ActiveCabs.query().get()

		def sync(key):
			update_cabs_array = cabs_memory_array

			# write to NDB:
			json_arr = Utils.items_to_json(update_cabs_array)
			if (key):
				key.cabs_array_ndb = json_arr
				key.put()
			else:
				key = ActiveCabs(cabs_array_ndb = json_arr)
				key.put()

		tran = ndb.transaction(lambda: sync(array_from_ndb))