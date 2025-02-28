import splunk.search as search
import splunk.auth as auth
import sys
import time

username = sys.argv[1]
password = sys.argv[2]
q = sys.argv[3]

sk = auth.getSessionKey(username, password)

job = search.dispatch("search " + q, sessionKey=sk)

while not job.isDone:
    print "Job is still running."
    time.sleep(.5)

for r in job.results:
    for f in r.keys():
        print "%s=%s" % (f, r[f])
    print "----------"

job.cancel()
