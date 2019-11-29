import sys
import getopt
import csv

argumentList = sys.argv[1:]

unixOptions = "hf:s:t:d:c:"
gnuOptions = ["help", "file=", "station=", "transport=", "delay=", "cancelled="]


try:
    arguments, _ = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
    print(str(err))
    exit()

destinationFile = ""
station = ""
transport = ""
delay = ""
cancelled = ""

def usageGuide():
    print("split.py usage:")
    print("--help (-h):\t\tshow usage guide")
    print("--file (-f):\t\tset destination file\t\t\t\t\t\t(mandatory)")
    print("--station (-s):\t\tfilter on specific station\t\t\t(default: none)\t(optional)")
    print("--transport (-t):\tfilter on specific transport carrier\t\t(default: none)\t(optional)")
    print("--delay (-d):\t\tfilter on having equal to or greater than delay\t(default: none)\t(optional)")
    print("--cancelled (-c):\tfilter on cancelled or not (yes/no/both)\t(default: both)\t(optional)")

for arg, value in arguments:
    if arg in ('-h', "--help"):
        usageGuide()
        exit()
    elif arg in ('-f', '--file'):
        print("setting destination file to %s" % (value))
        destinationFile = value
    elif arg in ('-s', '--station'):
        print("filtering on station %s" % (value))
        station = value
    elif arg in ('-t', '--transport'):
        print("filtering on transport carrier %s" % (value))
        transport = value
    elif arg in ('-d', '--delay'):
        print("filtering on having delay equal to or greater than %s" % (value))
        delay = value
    elif arg in ('-c', '--cancelled'):
        if (value == 'yes'):
            print("filtering on cancelled only")
            cancelled = 'yes'
        elif (value == 'no'):
            print("filtering on not cancelled only")
            cancelled = 'no'
        else:
            usageGuide()
            exit()

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
