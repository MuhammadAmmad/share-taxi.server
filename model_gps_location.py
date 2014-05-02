
from google.appengine.ext import ndb
import traceback
import cgi
import sys
import string
import traceback
from datetime import datetime
from collections import OrderedDict
import time
import datetime


class Location(ndb.Model):
    longitude = ndb.StringProperty(required = True)
    latitude = ndb.StringProperty(required = True)
    date = ndb.DateTimeProperty(auto_now=True)
    androidID = ndb.StringProperty(required = True,indexed=True)
    lineNum = ndb.StringProperty(required= True)
    #direction = ndb.StringProperty(required= True,choices=['N','S'])
    isActive = ndb.BooleanProperty()




    def to_json(self):
        #dateStr = lambda: int(round(self.date.time() * 1000))
        #dateStr = self.date.strftime('%Y-%m-%d @ %H:%M:%S')
        timeVar = self.date
        timeUnix = time.mktime(timeVar.timetuple())
        result = OrderedDict([
                ("androidID",self.androidID),
                ("date",timeUnix),
                ("lineNum",self.lineNum),
                #("direction",self.direction),
    			("longitude",self.longitude),
    			("latitude",self.latitude)
    			])
        return result