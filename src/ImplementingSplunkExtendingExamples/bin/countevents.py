import splunk.Intersplunk as si

results, dummyresults, settings = si.getOrganizedResults()
keywords, options = si.getKeywordsAndOptions()

count = 0
for r in results:
    count += 1

count_rows = []
count_rows.append({'count': count})

si.outputResults(count_rows)
