import datetime
from datetime import timedelta
import csv
import matplotlib.pyplot as plt


all_paths = []

f = open("data/ns_paths.txt")
for line in f:
    split = line.split(',')
    all_paths.append([split[0].split(' '), split[1].replace('\n', '').split(' ')[1:]])

station = 'ASD'

regular_trains = []
for p in all_paths:
    # if the current station is in the current route, and is not on the start
    # or end of the route(but somewhere in the middle)
    if (station in p[0][1:len(p[0]) - 1] and len(p[1]) > 30):
        regular_trains.append(p)

#
# train_delays = {}
# for p in regular_trains:
#     for train_number in p[1]:
#         train_delays.update({train_number: [[], []]})
#
# print(train_delays)
#
# f = open("data/ams_centraal.csv")
# for l in f:
#     l = l.split(',')
#     if l[2] in train_delays:
#         print("old", train_delays[l[2]])
#         train_delays[l[2]][0].append((str(l[0]) + ' ' + str(l[6])))
#         train_delays[l[2]][1].append()
#         print("new", train_delays[l[2]], "\n")

f = open("data/ams_centraal.csv")
lines = []
for l in f:
    l = l.split(',')
    lines.append(l)

lines = sorted(lines, key = lambda x: (x[0], x[6]))

datetimes = []
delays = []
total_delay = 0
for l in lines:
    Format = '%Y-%m-%d %H:%M:%S'
    time = l[0] + ' ' + l[6]
    total_delay = total_delay + int(l[7])
    datetimes.append(datetime.datetime.strptime(time, Format))
    delays.append(total_delay)

# datetimes = plt.dates.date2num(datetimes)

plt.plot(datetimes, delays)
plt.xlabel("time")
plt.ylabel("total minutes of delay")
plt.show()

# print(train_delays)
