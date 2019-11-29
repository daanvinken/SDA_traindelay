# libraries we need
import sys
import getopt
import csv

# get arguments
argumentList = sys.argv[1:]

# define allowed arguments
unixOptions = ""
gnuOptions = ["help", "file=", "date=", "hour=", "daterange=", "station=",
            "number=", "transporter=", "vehicle=", "destination=", "delay=",
            "cancelled=", "limit="]

# usage guide
def usageGuide():
    print("split.py usage:")
    print("--help:\t\tshow usage guide")
    print("--file:\t\tset destination file (x.csv)\t\t\t\t\t\t(mandatory)")
    print("--date:\t\tfilter on specific date (yyyy-mm-dd)\t\t\t(default: none)\t(optional)")
    print("--hour:\t\tfilter on specific hour of the day (h)\t\t\t(default: none)\t(optional)")
    print("--daterange:\tfilter to within specific dates (yyyy-mm-dd:yyyy-mm-dd)\t(default: none)\t(optional)")
    print("--station:\tfilter on specific station (shortened)\t\t\t(default: none)\t(optional)")
    print("--number\tfilter on specific train number (integer)\t\t(default: none)\t(optional)")
    print("--transporter:\tfilter on specific transport carrier (NS/Arriva/..)\t(default: none)\t(optional)")
    print("--vehicle:\tfilter on specific vehicle type (Sprinter/Intercity/..)\t(default: none)\t(optional)")
    print("--destination:\tfilter on specific destination (full name)\t\t(default: none)\t(optional)")
    print("--delay:\tfilter on having >= delay (integer)\t\t\t(default: none)\t(optional)")
    print("--cancelled:\tfilter on cancelled or not (yes/no/both)\t\t(default: both)\t(optional)")
    print("--limit:\tlimit amount of results (integer)\t\t\t(default: none)\t(optional)")

# check that we get commands in the right format
try:
    arguments, _ = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
    print(str(err))
    usageGuide()
    exit()

# parameters we extract from the command line
destinationFile = False
date = False
dateRange = False
hour = False
station = False
number = False
transporter = False
vehicle = False
destination = False
delay = False
cancelled = False
limit = False

for arg, value in arguments:
    if arg == '--help':
        usageGuide()
        exit()
    elif arg == '--file':
        print("setting destination file to %s" % (value))
        destinationFile = value
    elif arg == '--date':
        print("filtering on date %s" % (value))
        date = value
    elif arg == '--hour':
        print("filtering on hour %s:00" % (value))
        hour = int(value)
    elif arg == '--daterange':
        dateRange = value.split(':')
        print("filtering on range ", dateRange[0], " to ", dateRange[1])
    elif arg == '--station':
        print("filtering on station %s" % (value))
        station = value
    elif arg == '--number':
        print("filtering on train number %s" % (value))
        number = value
    elif arg == '--transporter':
        print("filtering on transport carrier %s" % (value))
        transporter = value
    elif arg == '--vehicle':
        print("filtering on vehicle type %s" % (value))
        vehicle = value
    elif arg == '--destination':
        print("filtering on destination %s" % (value))
        destination = value
    elif arg == '--delay':
        print("filtering on having delay equal to or greater than %s" % (value))
        delay = int(value)
    elif arg == '--cancelled':
        if (value == 'yes'):
            print("filtering on cancelled only")
            cancelled = '1'
        elif (value == 'no'):
            print("filtering on not cancelled only")
            cancelled = '0'
        elif (value != 'both'):
            usageGuide()
            exit()
    elif arg == '--limit':
        print("limiting output to %s entries" % (value))
        limit = int(value)

# having a destinationfile is mandatory
if (not destinationFile):
    print("destination flag required!")
    usageGuide()
    exit()

# we always use the same source file
with open('../data/vertrektijden.csv') as source_file:
    with open('../data/' + destinationFile, 'w') as dest_file:
        reader = csv.reader(source_file, delimiter=",")
        writer = csv.writer(dest_file)

        # index we need for keeping track of the limit
        index = 0

        for row in reader:
            # if we reach our limit, we kill the process
            if (limit and index >= limit):
                exit()
            
            # check if all parameters match
            if((not date or row[0] == date) and 
                (not station or row[1] == station) and
                (not number or row[2] == number) and
                (not transporter or row[3] == transporter) and
                (not vehicle or row[4] == vehicle) and
                (not destination or row[5] == destination) and
                (not hour or int(row[6].split(':')[0]) == hour) and
                (not dateRange or (row[0] >= dateRange[0] and row[0] <= dateRange[1])) and
                (not delay or int(row[7]) >= delay) and
                (not cancelled or row[8] == cancelled)):

                # write to file and increment index
                writer.writerow(list(row))
                index = index + 1
