# plot showing a scatterplot between amount of stops made per day, and amount of delayed stops made per day
import matplotlib.pyplot as plt
import csv
import datetime

# year, month, day = '2019-12-02'.split("-")
# print(datetime.date(int(year), int(month), int(day)).weekday())

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
        year, month, day = date.split("-")
        weekday = datetime.date(int(year), int(month), int(day)).weekday()

        delay = line[columns.index("delay")]

        if weekday not in total_trains:
            total_trains[weekday] = 1
        else:
            total_trains[weekday] = total_trains[weekday] + 1

        if int(delay) > 0:
            if weekday not in delayed_trains:
                delayed_trains[weekday] = 1
            else:
                delayed_trains[weekday] = delayed_trains[weekday] + 1

plt.bar(range(len(total_trains)), list(total_trains.values()), align='center', label="total amount of stops")
plt.bar(range(len(delayed_trains)), list(delayed_trains.values()), align='center', label="amount of delayed stops")
plt.xlabel("day of the week")
plt.legend()
plt.show()