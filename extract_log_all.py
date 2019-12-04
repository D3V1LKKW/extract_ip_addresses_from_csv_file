import csv
import sys

f = open(sys.argv[1])
csv_f = csv.reader(f)

for row in csv_f:
	print "{:<20s}{:<5s}{:>10s}".format(row[7], ":", row[31])