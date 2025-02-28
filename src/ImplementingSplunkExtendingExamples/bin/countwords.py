import splunk.Intersplunk as si
import re
import operator
from collections import defaultdict


class WordCounter:
    word_counts = defaultdict(int)
    unique_word_counts = defaultdict(int)
    rowcount = 0
    casesensitive = False
    mincount = 50
    minwordlength = 3

    def process_event(self, input):
        self.rowcount += 1
        words_in_event = re.findall('\W*([a-zA-Z]+)\W*', input)

        unique_words_in_event = set()
        for word in words_in_event:
            if len(word) < self.minwordlength:
                continue   # skip this word, it's too short
            if not self.casesensitive:
                word = word.lower()
            self.word_counts[word] += 1
            unique_words_in_event.add(word)

        for word in unique_words_in_event:
            self.unique_word_counts[word] += 1

    def build_sorted_counts(self):
        #create an array of tuples,
        #ordered by the count for each word
        sorted_counts = sorted(self.word_counts.iteritems(),
                               key=operator.itemgetter(1))
        #reverse it
        sorted_counts.reverse()

        return sorted_counts

    def build_rows(self):
        #build our results, which must be an array of dict
        count_rows = []
        for word, count in self.build_sorted_counts():
            if self.mincount < 1 or count >= self.mincount:
                unique = self.unique_word_counts.get(word, 0)
                percent = round(100.0 * unique / self.rowcount, 2)
                newrow = {'word': word,
                          'count': str(count),
                          'Events with word': str(unique),
                          'Event count': str(self.rowcount),
                          'Percent of events with word':
                          str(percent)}
                count_rows.append(newrow)
        return count_rows


#return an integer from an option, or raise useful Exception
def getInt(options, field, default):
    try:
        return int(options.get(field, default))
    except Exception, e:
        #raise a user friendly exception
        raise Exception("%s must be an integer" % field)


if __name__ == '__main__':
    try:
        #get our results
        results, dummyresults, settings = si.getOrganizedResults()
        keywords, options = si.getKeywordsAndOptions()

        word_counter = WordCounter()

        word_counter.mincount = getInt(options, 'mincount', 50)
        word_counter.minwordlength = getInt(options,
                                            'minwordlength', 3)

        #determine whether we should be case sensitive
        casesensitive = options.get('casesensitive', False)
        if casesensitive:
            casesensitive = (casesensitive.lower().strip() in
                             ['t', 'true', '1', 'y', 'yes'])
        word_counter.casesensitive = casesensitive

        #loop through the original results
        for r in results:
            word_counter.process_event(r['_raw'])

        output = word_counter.build_rows()
        si.outputResults(output)

    #catch the exception and show the error to the user
    except Exception, e:
        import traceback
        stack = traceback.format_exc()
        si.generateErrorResults("Error '%s'. %s" % (e, stack))
