import webapp2

# Handlers
# from feed_handler import FeedHandler
from PostLocHandler import PostLocHandler
from GetLocHandler import GetLocHandler
from stopDeviceHandler import stopDeviceHandler
# from image_handler import ImageHandler
#from homepage_handler import HomepageHandler

app = webapp2.WSGIApplication([#('/', HomepageHandler),
                              #('/newDev', NewDeviceHandler),
                              ('/postLocation', PostLocHandler),
                              #('/showLocations',showLocations),
                              ('/getLocations',GetLocHandler),
                              ('/stopDevice',stopDeviceHandler)
                               # ('/blobphoto/([^/]+)?', BlobImageServeHandler),
                               # ('/votes/new', VoteHandler),
                               # ('/feed', FeedHandler),
                               ],
                              debug=True)