import splunk.Intersplunk

results, dummyresults, settings = splunk.Intersplunk.getOrganizedResults()
splunk.Intersplunk.outputResults(results)
