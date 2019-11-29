import matplotlib.pyplot as plt
import csv

columns = [
    "date", "station", "trainnumber", "company",
    "traintype", "destination", "delay", "canceled"
]

# Dictionary contains dates as keys and sets of trainnumbers as values
total_trains = {}
delayed_trains = {}

with open("../data/trains_2019_08_01_to_2019_11_01.csv") as vertrektijden:
    reader = csv.reader(vertrektijden, delimiter=",")

    for line in reader:

        date = line[columns.index("date")]
        trainnumber = line[columns.index("trainnumber")]

        if date not in total_trains:
            total_trains[date] = set()

        total_trains[date].add(trainnumber)

    for date in total_trains:
        total_trains[date] = len(total_trains[date])

with open("../data/delayed_trains_2019_08_01_to_2019_11_01.csv") as vertrektijden:
    reader = csv.reader(vertrektijden, delimiter=",")

    for line in reader:

        date = line[columns.index("date")]
        trainnumber = line[columns.index("trainnumber")]

        if date not in delayed_trains:
            delayed_trains[date] = set()

        delayed_trains[date].add(trainnumber)

    for date in delayed_trains:
        delayed_trains[date] = len(delayed_trains[date])

plt.plot(range(len(delayed_trains.keys())), list(delayed_trains.values()), label="delay")
plt.plot(range(len(total_trains.keys())), list(total_trains.values()), label="total")
plt.ylabel("Occurences")
plt.xlabel("Dates")
plt.legend()
plt.show()
