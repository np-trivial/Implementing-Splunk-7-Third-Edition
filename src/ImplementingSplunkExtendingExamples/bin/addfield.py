#import the python module provided with Splunk
import splunk.Intersplunk as si

#read the results into a variable
results, dummyresults, settings = si.getOrganizedResults()

#loop over each result. results is a list of dict.
for r in results:
    #r is a dict. Access fields using the fieldname.
    r['foo'] = 'bar'

#return the results back to Splunk
si.outputResults(results)
