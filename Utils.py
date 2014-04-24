from google.appengine.ext import ndb
from google.appengine.api import urlfetch


class Utils():
    @staticmethod
    def items_to_json(items):
      arr = []
      for item in items:
        arr.append(item.to_json())
      return arr

    