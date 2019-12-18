# get_paths returns all train routes

import datetime
from datetime import timedelta
from statistics import mode
import csv

def parse_line(line):
    return line.split(",")

def time_diff(previous, current):
    Format = '%Y-%m-%d %H:%M:%S'
    d1 = previous[1] + ' ' + previous[2]
    d2 = current[1] + ' ' + current[2]
    diff = datetime.datetime.strptime(d2, Format) - datetime.datetime.strptime(d1, Format)
    return diff.seconds

def same_path(previous, current):
    # big time between stations
    if time_diff(previous, current) > (4*60*60):
        return False
    # destination is different
    elif previous[3] != current[3]:
        return False
    return True

def most_frequent(llist):
    counter = 0
    num = llist[0]
    for i in llist:
        curr_frequency = llist.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i
    return num

def station_data():
    result = []
    with open('data/Adressen_Stations.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                result.append([row[0], row[1], row[2], row[3]])
    return result

def abbr(name, table):
    abbr = [n[1] for n in table if n[0] == name]
    if len(abbr) != 0:
        return abbr[0]
    print("couldn't find abbreviation for", name)
    return []

def get_paths(filepath):
    train_routes = {}
    all_paths = []
    i = 0

    with open(filepath) as FileObj:
        for line in FileObj:
            # if (i > 100000):
            #     break
            # else:
            #     i += 1

            # Parse line
            # Date, Station, Train number, Transport company, Train type,
            # Destination, Delay in minutes, cancelled(1=yes, 0=no)
            l = parse_line(line)

            # If train number is not yet known, it takes a new route. Add
            # the train number to the train-route dict.
            # Else If the train number is known, add the station to the values
            # for the train number
            if l[2] not in train_routes:
                train_routes.update({l[2] : [[l[1], l[0], l[6], l[5]]]})
            else:
                train_routes[l[2]] = train_routes[l[2]] + [[l[1], l[0], l[6], l[5]]]

    # Sort the train routes in the dictionairy, and get each different route
    for train_nr in train_routes:
        train_routes[train_nr] = sorted(train_routes[train_nr],key=lambda l:(l[1], l[2]))

        paths = []
        path = []

        # Get each path a train has travelled
        for station, date, time, destination in train_routes[train_nr]:
            # if the current station is the first train station, make a new
            # path
            if not path:
                path = [station]
            # If it is not the first station of a path, but it does belong with
            # the current path, ppend it to the previous stations of this path
            elif same_path(previous, [station, date, time, destination]):
                path.append(station)
            # If the current station is not part of the current path, save
            # the old path and create a new one with the current station.
            else:
                paths.append([path, destination])
                path = [station]

            previous = [station, date, time, destination]

        if len(paths) != 0:
            path = most_frequent(paths)
            # If path is already in the list, add the train_nr to this list.
            # If the path is not in the list, make a new element in the list.
            P = [p[0] for p in all_paths]
            if path in P:
                i = P.index(path)
                all_paths[i] = [all_paths[i][0], all_paths[i][1] + [train_nr]]
            else:
                all_paths.append([path, [train_nr]])

    # Table for converting the names to abbreviations(and the other way around)
    # for all stations
    stations = station_data()
    table = [[station[0], station[1]] for station in stations]
    table = table + [['Arnhem Centraal', 'AH'], ['Schiphol Airport', 'SHL'], ['\'s-Hertogenbosch', 'HT'], ['\'t Harde', 'HDE']]

    # Convert the destination of each path to it's abbreviation. Each path now
    # shows all stations in it's path, instead of all but the final one.
    for i in range(len(all_paths)):
        all_paths[i] = [all_paths[i][0][0] + [abbr(all_paths[i][0][1], table)], all_paths[i][1]]

    f = open("data/ns_paths.txt", "w+")
    for path in all_paths:
        f.write(' '.join(path[0]) + ", " + ' '.join(path[1]) + '\n')

    return all_paths
