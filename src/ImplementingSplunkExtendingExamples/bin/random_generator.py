import splunk.Intersplunk as si
from random import randint

keywords, options = si.getKeywordsAndOptions()


def getInt(options, field, default):
    try:
        return int(options.get(field, default))
    except Exception, e:
        #raise a user friendly exception
        raise Exception("%s must be an integer" % field)


try:
    min = getInt(options, 'min', 0)
    max = getInt(options, 'max', 1000000)
    eventcount = getInt(options, 'eventcount', 100)

    results = []
    for r in range(0, eventcount):
        results.append({'r': randint(min, max)})

    si.outputResults(results)

except Exception, e:
    import traceback
    stack = traceback.format_exc()
    si.generateErrorResults("Error '%s'. %s" % (e, stack))
