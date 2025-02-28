import sys
import re
from csv import DictReader
from csv import DictWriter

patterns = []


def add_pattern(pattern, section):
    patterns.append((re.compile(pattern), section))

add_pattern('^/about/.*', 'about')
add_pattern('^/contact/.*', 'contact')
add_pattern('^/.*/.*', 'unknown_non_root')
add_pattern('^/.*', 'root')
add_pattern('.*', 'nomatch')


# return a section for this url
def lookup(url):
    try:
        for (pattern, section) in patterns:
            if pattern.match(url):
                return section
        return ''
    except:
        return ''


#set up our reader
reader = DictReader(sys.stdin)
fields = reader.fieldnames

#set up our writer
writer = DictWriter(sys.stdout, fields)
writer.writeheader()

#start our output
call_count = 0
for row in reader:
    call_count = call_count + 1

    if len(row['url']):
        row['section'] = lookup(row['url'])
        row['call_count'] = call_count
        writer.writerow(row)
