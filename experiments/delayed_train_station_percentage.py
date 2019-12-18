import csv
import math

def parse_line(line):
    return line.split(",")

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

# create lookup table for full station names
name_table = {}
for name in station_data():
    name_table.update({name[1] : name[0]})


stations = {}

filepath = "data/ns.csv"
with open(filepath) as FileObj:
    for line in FileObj:
        l = parse_line(line)

        if l[1] not in stations:
            # station name : [minutes of delay, train stops]
            stations.update({l[1] : [0, 0]})
        stations[l[1]][0] += int(l[7])
        stations[l[1]][1] += 1

station_delays = []
for s in stations:
    delay_per_stop = (stations[s][0]*60) / stations[s][1]
    if s in name_table:
        name = name_table[s]
    else:
        name = s
    station_delays.append([name, delay_per_stop, stations[s][1], s])

station_delays = [s for s in station_delays if s[2] >= 10000]
station_delays = sorted(station_delays, key = lambda x: x[1], reverse=True)


print("\n\n%-25s %-10s %-7s\n" % ("station", "ave delay", "stops"))
for s in station_delays:
    sec = int(s[1]) % 60
    min = math.floor(int(s[1]) / 60)
    delay = ""
    if min:
        delay = delay + str(min) + "m "
    if sec:
        delay = delay + str(sec) + "s"

    print("%-25s %-10s %-7i" % (s[0], delay, s[2]))
