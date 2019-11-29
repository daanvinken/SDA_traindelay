import sys
import getopt
import csv

argumentList = sys.argv[1:]

unixOptions = ""
gnuOptions = ["help", "file=", "date=", "station=", "number=", "transporter=",
            "vehicle=", "destination=", "delay=", "cancelled="]

def usageGuide():
    print("split.py usage:")
    print("--help:\t\tshow usage guide")
    print("--file:\t\tset destination file\t\t\t\t\t\t(mandatory)")
    print("--station:\tfilter on specific station\t\t\t(default: none)\t(optional)")
    print("--number\tfilter on specific train number\t\t\t(default: none)\t(optional)")
    print("--transporter:\tfilter on specific transport carrier\t\t(default: none)\t(optional)")
    print("--vehicle:\tfilter on specific vehicle type\t\t\t(default: none)\t(optional)")
    print("--destination:\tfilter on specific destination\t\t\t(default: none)\t(optional)")
    print("--delay:\tfilter on having equal to or greater than delay\t(default: none)\t(optional)")
    print("--cancelled:\tfilter on cancelled or not (yes/no/both)\t(default: both)\t(optional)")

try:
    arguments, _ = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
    print(str(err))
    usageGuide()
    exit()

destinationFile = ""
date = ""
station = ""
number = ""
transporter = ""
vehicle = ""
destination = ""
delay = ""
cancelled = ""

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
        delay = value
    elif arg == '--cancelled':
        if (value == 'yes'):
            print("filtering on cancelled only")
            cancelled = 'yes'
        elif (value == 'no'):
            print("filtering on not cancelled only")
            cancelled = 'no'
        elif (value != 'both'):
            usageGuide()
            exit()

# having a destinationfile is mandatory
if (destinationFile == ""):
    usageGuide()
    exit()


exit()

with open('../data/vertrektijden.csv') as source_file:
    with open('../data/vertrektijden_unquoted.csv', 'w') as dest_file:
        reader = csv.reader(source_file, delimiter=";")
        writer = csv.writer(dest_file)

        for row in reader:
            writer.writerow(list(row))

with open('../data/vertrektijden.csv') as source_file:
    with open('../data/vertragingen.csv', 'w') as dest_file:
        reader = csv.reader(source_file, delimiter=";")
        writer = csv.writer(dest_file)

        for row in reader:
            if (row[7] != '0'):
                writer.writerow(list(row))

with open('../data/vertrektijden.csv') as source_file:
    with open('../data/geenvertragingen.csv', 'w') as dest_file:
        reader = csv.reader(source_file, delimiter=";")
        writer = csv.writer(dest_file)

        for row in reader:
            if (row[7] == '0'):
                writer.writerow(list(row))
