# histogram showing amount of delayed stops per weekday
import matplotlib.pyplot as plt
import csv
import datetime

columns = [
    "date", "station", "trainnumber", "company",
    "traintype", "destination", "time", "delay", "canceled"
]

# Dictionary contains dates as keys and sets of trainnumbers as values
delayed_trains = {}

with open("../data/vertrektijden.csv") as vertrektijden:
    reader = csv.reader(vertrektijden, delimiter=",")

    for line in reader:

        date = line[columns.index("date")]
        year, month, day = date.split("-")
        weekday = datetime.date(int(year), int(month), int(day)).weekday()

        # filtering out weekends
        if (weekday >= 5): continue

        delay = line[columns.index("delay")]

        if int(delay) > 0:
            if date not in delayed_trains:
                delayed_trains[date] = 1
            else:
                delayed_trains[date] = delayed_trains[date] + 1

plt.hist(delayed_trains.values(), 25)
plt.ylabel("Occurences")
plt.xlabel("Amount of delayed stops per day")
plt.show()
