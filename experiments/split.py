import sys
import getopt
import csv

argumentList = sys.argv[1:]

unixOptions = ""
gnuOptions = ["help", "file=", "date=", "hour=", "station=", "number=", "transporter=",
            "vehicle=", "destination=", "delay=", "cancelled=", "limit="]

def usageGuide():
    print("split.py usage:")
    print("--help:\t\tshow usage guide")
    print("--file:\t\tset destination file\t\t\t\t\t\t(mandatory)")
    print("--date:\t\tfilter on specific date\t\t\t\t(default: none)\t(optional)")
    print("--hour:\t\tfilter on specific hour of the day\t\t(default: none)\t(optional)")
    print("--station:\tfilter on specific station\t\t\t(default: none)\t(optional)")
    print("--number\tfilter on specific train number\t\t\t(default: none)\t(optional)")
    print("--transporter:\tfilter on specific transport carrier\t\t(default: none)\t(optional)")
    print("--vehicle:\tfilter on specific vehicle type\t\t\t(default: none)\t(optional)")
    print("--destination:\tfilter on specific destination\t\t\t(default: none)\t(optional)")
    print("--delay:\tfilter on having equal to or greater than delay\t(default: none)\t(optional)")
    print("--cancelled:\tfilter on cancelled or not (yes/no/both)\t(default: both)\t(optional)")
    print("--limit:\tlimit amount of results\t\t\t\t(default: none)\t(optional)")

try:
    arguments, _ = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
    print(str(err))
    usageGuide()
    exit()

destinationFile = False
date = False
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
    elif arg =='--hour':
        print("filtering on hour %s:00" % (value))
        hour = int(value)
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
if (destinationFile == ""):
    usageGuide()
    exit()

with open('../data/vertrektijden.csv') as source_file:
    with open('../data/' + destinationFile, 'w') as dest_file:
        reader = csv.reader(source_file, delimiter=",")
        writer = csv.writer(dest_file)

        index = 0

        for row in reader:
            if (limit and index >= limit):
                exit()
            if((not date or row[0] == date) and 
                (not station or row[1] == station) and
                (not number or row[2] == number) and
                (not transporter or row[3] == transporter) and
                (not vehicle or row[4] == vehicle) and
                (not destination or row[5] == destination) and
                (not hour or int(row[6].split(':')[0]) == hour) and
                (not delay or int(row[7]) >= delay) and
                (not cancelled or row[8] == cancelled)):
                writer.writerow(list(row))
                index = index + 1
