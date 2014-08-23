import webapp2

from post_location_handler import PostLocHandler
from get_location_handler import GetLocHandler
from stop_device_handler import stopDeviceHandler
from start_device_handler import startDeviceHandler
from homepage_handler import HomepageHandler
from upd_cab_occupation import updCabOccupation
from sync_mem_ndb import syncMemNdb
from test1Handler import Test1Handler
from test2Handler import Test2Handler
from stop_cab_manually import StopTestsCabHandler

app = webapp2.WSGIApplication([('/', HomepageHandler),
                              ('/postLocation', PostLocHandler),
                              ('/getLocations',GetLocHandler),
                              ('/stopDevice',stopDeviceHandler),
                              ('/startDevice',startDeviceHandler),
                              ('/updCabOccupation',updCabOccupation),
                              ('/syncMemNdb',syncMemNdb),
                              ('/test1', Test1Handler),
                              ('/test2', Test2Handler),
                              ('/removeCab', StopTestsCabHandler)
                              ],
                              debug=True)
