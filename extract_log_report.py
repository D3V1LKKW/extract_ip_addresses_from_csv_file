import csv
import sys

f = open(sys.argv[1])
csv_f = csv.reader(f)

flag = 1

for row in csv_f:
	if flag == 1:
		print "{:<20s}{:<5s}{:>10s}".format(row[0], ":", row[1])
		flag = 0
	else:
		if int(row[1]) > 307200:
			print "{:<20s}{:<5s}{:>10s}".format(row[0], ":", row[1])