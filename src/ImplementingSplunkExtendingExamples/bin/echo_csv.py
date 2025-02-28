import sys
import csv

r = csv.reader(sys.stdin)
w = csv.writer(sys.stdout)

for l in r:
    w.writerow(l)

#this example script does nothing but echo the results
