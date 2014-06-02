import datetime
import webapp2

from google.appengine.ext import ndb
from model_cabs_memory import *
from model_cabs_ndb import *
from Utils import *

class syncMemNdb(webapp2.RequestHandler):
	def get(self):
		
		#TODO: add transaction!!
		update_cabs_array = []

		# read from NDB:
		array_from_ndb = ActiveCabs.query().get()

		#TODO: make update_cabs_array the update one+ check for dates
		# create new update array:
		update_cabs_array = cabs_memory_array


		#TODO:
		# write to memory:
		#cabs_memory_array = update_cabs_array

		# write to NDB:
		json_arr = Utils.items_to_json(update_cabs_array)
		if (array_from_ndb):
			array_from_ndb.cabs_array_ndb = json_arr
			array_from_ndb.put()
		else:
			curr_arr = ActiveCabs(cabs_array_ndb = json_arr)
			curr_arr.put()