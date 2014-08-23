import webapp2

from model_cabs_memory import *

class StopTestsCabHandler(webapp2.RequestHandler):

	def get(self):
		cabID = self.request.get("id", default_value='0')
		print('cabID:', cabID)
		for cab in cabs_memory_array:
			if (cab.androidID=='1234' or cab.androidID=='4567' or cab.androidID=='0000' or cab.androidID=='1111' or cab.androidID==cabID):
				print('removed cab:', cab.androidID)
				cabs_memory_array.remove(cab)