import json
import webapp2
import cgi
import urllib
import urllib2
import jinja2
import os
import sys
import string
import traceback
import time
import logging
import datetime

from model_cabs_memory import *

class Test1Handler(webapp2.RequestHandler):

    def get(self):

        latlngs = [['32.069430', '34.770553'],['32.070958', '34.769781'],
                   ['32.071903', '34.769352'],['32.072776', '34.768665'],
                   ['32.074885', '34.767978'],['32.077649', '34.768493'],
                   ['32.077649', '34.768493'],['32.079194', '34.769333'],
                   ['32.079194', '34.769333'],['32.083594', '34.771822'],
                   ['32.084976', '34.772509'],['32.077649', '34.768493'],
                   ['32.081703', '34.770810'],['32.082794', '34.771282'],
                   ['32.083849', '34.771840'],['32.086649', '34.772956'],
                   ['32.087703', '34.773171'],['32.088612', '34.773557'],
                   ['32.089630', '34.773900'],['32.089630', '34.773900'],
                   ['32.091157', '34.774287'],['32.092539', '34.774716'],
                   ['32.092539', '34.774716'],['32.095847', '34.776089'],
                   ['32.097338', '34.775874'],['32.098356', '34.778894'],
                   ['32.098610', '34.781383'],['32.098610', '34.781383']]

        cab_not_in_array = True
        curr_date = datetime.datetime.now()

        for cab in cabs_memory_array:
            if (cab.androidID == '1234'):
                cab_not_in_array = False
                temp = cab
                print('cab exists')
                if (temp.date < curr_date):
                    temp.update_cab(curr_date, latlngs[0][1],latlngs[0][0])

        if (cab_not_in_array):
            temp = cabObject('1234',curr_date,'4',latlngs[0][1],latlngs[0][0])
            cabs_memory_array.append(temp)
            print('new cab added')
        
        for i in range(len(latlngs)):
            curr_date = datetime.datetime.now()
            temp.update_cab(curr_date, latlngs[i][1],latlngs[i][0])
            print('update',i)
            time.sleep(2) # delay 2 seconds
