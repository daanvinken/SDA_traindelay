# plot showing a scatterplot between amount of stops made per day, and amount of delayed stops made per day
import matplotlib.pyplot as plt
import csv

columns = [
    "date", "station", "trainnumber", "company",
    "traintype", "destination", "time", "delay", "canceled"
]

# Dictionary contains dates as keys and sets of trainnumbers as values
total_trains = {}
delayed_trains = {}

with open("../data/vertrektijden.csv") as vertrektijden:
    reader = csv.reader(vertrektijden, delimiter=",")

    for line in reader:

        date = line[columns.index("date")]
        delay = line[columns.index("delay")]

        if date not in total_trains:
            total_trains[date] = 1
        else:
            total_trains[date] = total_trains[date] + 1

        if int(delay) > 0:
            if date not in delayed_trains:
                delayed_trains[date] = 1
            else:
                delayed_trains[date] = delayed_trains[date] + 1

plt.scatter(total_trains.values(), delayed_trains.values(), alpha=0.1)
plt.ylabel("Amount of delayed stops per day")
plt.xlabel("Amount of stops per day")
plt.show()