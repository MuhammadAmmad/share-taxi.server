import webapp2

from post_location_handler import PostLocHandler
from get_location_handler import GetLocHandler
from stop_device_handler import stopDeviceHandler
from start_device_handler import startDeviceHandler
from homepage_handler import HomepageHandler
from upd_cab_occupation import updCabOccupation
from sync_mem_ndb import syncMemNdb

app = webapp2.WSGIApplication([('/', HomepageHandler),
                              ('/postLocation', PostLocHandler),
                              ('/getLocations',GetLocHandler),
                              ('/stopDevice',stopDeviceHandler),
                              ('/startDevice',startDeviceHandler),
                              ('/updCabOccupation',updCabOccupation),
							  ('/syncMemNdb',syncMemNdb)
                               ],
                              debug=True)