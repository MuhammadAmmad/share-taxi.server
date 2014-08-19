import time
import datetime
from collections import OrderedDict

class cabsGlobalArr(object):
	global cabs_memory_array
	cabs_memory_array = []

class cabObject(object):
	def __init__(self, androidID, date, line, longt, lat):
		self.androidID = androidID
		self.date = date
		self.lineNum = line
		self.longitude = longt
		self.latitude = lat
		self.freeSeats = None

	def update_cab(self,date,longt,lat):
		self.date = date
		self.longitude = longt
		self.latitude = lat

	def update_freeSeats(self,freeSeats):
		self.freeSeats = freeSeats

	def to_json(self):
		timeVar = self.date
		timeUnix = time.mktime(timeVar.timetuple())
		result = OrderedDict([
            ("androidID",self.androidID),
            ("date",timeUnix),
            ("lineNum",self.lineNum),
      		("longitude",self.longitude),
      		("latitude",self.latitude),
      		("freeSeats",self.freeSeats)
      		])
		return result