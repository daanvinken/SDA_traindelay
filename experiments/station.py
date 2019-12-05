# plot showing amount of stops and delays per station
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

plt.bar(*zip(*total_trains.items()), align='center', label="total amount of stops")
plt.bar(*zip(*delayed_trains.items()), align='center', label="amount of delayed stops")
plt.tick_params(axis='x', labelbottom=False, bottom=False)
plt.xlabel("different stations")
plt.legend()
plt.show()