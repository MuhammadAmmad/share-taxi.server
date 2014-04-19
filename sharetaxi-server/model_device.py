
from google.appengine.ext import ndb
from model_gps_location import Location


class Device(ndb.Model):
    id = ndb.IntegerProperty(required = True)
    name = ndb.StringProperty()
	#curr_location = ndb.KeyProperty(kind=Location,repeated=True)


# loc = Location(longitude=-122.084095,latitude=37.422006)
# dev = Device(id=1,name-'lim',curr_location=loc)
# dev.put()

def searchDevice(id):
    Device_query = Device.query(Device.id == id)
    if not Device_query:
    	return null
    dev = Device_query.fetch(10)
    return dev


# class statDevice(object)
# 	@staticmethod
# 	def insDevice():
# 		#global dev
#     	dev = Device(id=1,name='lim')
#     	dev.put()





   





