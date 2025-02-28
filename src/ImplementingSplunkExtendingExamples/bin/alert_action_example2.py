#!/usr/bin/env python

import sys
from csv import DictReader
import gzip
import urllib
import urllib2
import json

#our ticket system url
open_ticket_url = "http://ticketsystem.mygreatcompany/ticket"

#open the gzip as a file
f = gzip.open(sys.argv[8], 'rb')

#create our csv reader
reader = DictReader(f)
for event in reader:
    fields = {'json': json.dumps(event),
              'name': sys.argv[4],
              'count': sys.argv[1]}
    #build the POST data
    data = urllib.urlencode(fields)

    #the request will be a post
    resp = urllib2.urlopen(open_ticket_url, data)
    print resp.read()

f.close()
