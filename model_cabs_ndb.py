import json
from google.appengine.ext import ndb

class ActiveCabs(ndb.Model):
    cabs_array_ndb = ndb.JsonProperty(repeated = True)