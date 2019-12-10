#bins by default on 51 for max 50 minutes delay (one bar per minute)

# libraries we need
import sys
import getopt
import csv
import matplotlib.pyplot as plt

# get arguments
argumentList = sys.argv[1:]

# define allowed arguments
unixOptions = ""
gnuOptions = ["max_delay=", "bins=", "file=","log="]

# check that we get commands in the right format
try:
    arguments, _ = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
    print(str(err))
    exit()

#default values
max_delay = 800
bins = 100

for arg, value in arguments:
    if arg == '--max_delay':
        print("setting max delay time to %s" % (value))
        max_delay = value
    if arg == '--bins':
        print("setting max delay time to %s" % (value))
        bins = value

delayList = []

# we always use the same source file
with open('../data/delay.csv') as source_file:
    reader = csv.reader(source_file, delimiter=",")
    for row in reader:
            # write to list
        vertraging = int(row[7])
        cancelled = int(row[8])
        if (vertraging <= max_delay):
            delayList.append(vertraging)
            if (vertraging > 30):
                print(row)


plt.hist(delayList, bins=bins)
plt.yscale("log")
plt.xscale("log")
plt.xlabel("Delay in minutes (excluding cancelled trains)")
plt.ylabel("Occurences (log)")
plt.show()

