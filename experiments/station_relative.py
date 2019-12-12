# histogram showing amount of delays divided by stops per station
import matplotlib.pyplot as plt
import csv
import datetime

columns = [
    "date", "station", "trainnumber", "company",
    "traintype", "destination", "time", "delay", "canceled"
]

# Dictionary contains stations as keys and occurences as values
total_trains = {}
delayed_trains = {}

with open("../data/vertrektijden.csv") as vertrektijden:
    reader = csv.reader(vertrektijden, delimiter=",")

    for line in reader:

        station = line[columns.index("station")]

        delay = line[columns.index("delay")]

        if station not in total_trains:
            total_trains[station] = 1
        else:
            total_trains[station] = total_trains[station] + 1

        if int(delay) > 0:
            if station not in delayed_trains:
                delayed_trains[station] = 1
            else:
                delayed_trains[station] = delayed_trains[station] + 1

relative_delays = []
for key in total_trains.keys():
    relative_delays.append(delayed_trains.get(key, 0) / total_trains[key])

plt.hist(relative_delays, 20)
plt.xlabel("percentage of trains delayed per station")
plt.ylabel("occurences")
plt.show()