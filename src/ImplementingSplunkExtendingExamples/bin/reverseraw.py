import splunk.Intersplunk as si
import re


#since we're not writing a proper class, functions need to be
#defined first
def reverse(s):
    return s[::-1]

#start the actual script
results, dummyresults, settings = si.getOrganizedResults()
#retrieve any options included with the command
keywords, options = si.getKeywordsAndOptions()

#get the value of words, defaulting to false
words = options.get('words', False)
#validate the value of words
if words and words.lower().strip() in ['t', 'true', '1', 'yes']:
    words = True
else:
    words = False

#loop over the results
for r in results:
    #if the words option is true, then reverse each word
    if words:
        newRaw = []
        parts = re.split('([^a-zA-Z\']+)', r['_raw'])
        for n in range(0, len(parts) - 2, 2):
            newRaw.append(reverse(parts[n]))
            newRaw.append(parts[n + 1])
        newRaw.append(reverse(parts[-1]))
        r['_raw'] = ''.join(newRaw)
    #otherwise simply reverse the entire value of _raw
    else:
        r['_raw'] = reverse(r['_raw'])

si.outputResults(results)
