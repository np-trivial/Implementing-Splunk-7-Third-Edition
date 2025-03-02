import time
import random
import os
import re
import base64

start = time.time() - 13000

pwd = os.path.dirname(__file__)

outputpath = os.path.normpath(pwd + '/../sample_data/impl_splunk_web.log')
if(os.path.exists(outputpath)):
    exit(0)

inputpath = outputpath + '.noDates'
inputfile = open(inputpath, 'r')
outputfile = open(outputpath, 'w')

#1 user=#user# GET /foo?q=#q# uid=#uid#

uidcache = {}
for l in inputfile.readlines():
    parts = re.findall('^(\d+)\s+(.*)', l)
    fromnow = int(parts[0][0]) + random.randrange(-5, 5)
    event = parts[0][1]

    user = random.sample(['user1',
                          'user2',
                          'user3',
                          'user4',
                          'bobby'], 1)[0]

    q = random.randrange(2, 15)
    if random.randrange(1, 100) is 1:
        q = 1

    restartSession = random.randrange(1, 3) is 1

    if (user not in list(uidcache.keys())) or (q is 1 and restartSession):
        uid = base64.b64encode(
            str(
                random.randrange(1000000, 5000050)
            )
        ).replace('==', '')
        uidcache[user] = uid
    else:
        uid = uidcache[user]

    newline = time.strftime('%Y-%m-%dT%H:%M:%S',
                            time.gmtime(start + fromnow)) + " " + event
    newline = newline.replace('#user#', user).\
        replace('#q#', str(q)).\
        replace('#uid#', uid)

    outputfile.write(newline + "\n")
#    print newline

outputfile.close()

#time.strftime('%Y-%m-%dT%H:%M:%S',time.gmtime( start + 90 ) )
