#histogram showing difference of stops and delays per monday + tuesday
import matplotlib.pyplot as plt
import csv
import datetime

columns = [
    "date", "station", "trainnumber", "company",
    "traintype", "destination", "time", "delay", "cancelled"
]

# Dictionary contains dates as keys and occurences as values
total_trains = {}
delayed_trains = {}

with open("../data/vertrektijden.csv") as vertrektijden:
    reader = csv.reader(vertrektijden, delimiter=",")

    for line in reader:

        date = line[columns.index("date")]
        delay = line[columns.index("delay")]
        year, month, day = date.split("-")
        weekday = datetime.date(int(year), int(month), int(day)).weekday()

        # filtering out other days
        if (weekday > 1): continue

        if date not in total_trains:
            total_trains[date] = 1
            delayed_trains[date] = 0
        else:
            total_trains[date] = total_trains[date] + 1

        if int(delay) > 0:
            delayed_trains[date] = delayed_trains[date] + 1

total_mon = []
total_tues = []
total_diffs = []
delayed_mon = []
delayed_tues = []
delayed_diffs = []

for key in total_trains.keys():
    year, month, day = key.split("-")
    weekday = datetime.date(int(year), int(month), int(day)).weekday()

    if (weekday == 0):
        total_mon.append(total_trains[key])
    else:
        total_tues.append(total_trains[key])       

for i in range(len(total_mon)):
    total_diffs.append(total_mon[i] - total_tues[i])

for key in delayed_trains.keys():
    year, month, day = key.split("-")
    weekday = datetime.date(int(year), int(month), int(day)).weekday()

    if (weekday == 0):
        delayed_mon.append(delayed_trains[key])
    else:
        delayed_tues.append(delayed_trains[key])       

for i in range(len(delayed_mon)):
    delayed_diffs.append(delayed_mon[i] - delayed_tues[i])

plt.hist(total_diffs, alpha=0.5, label="difference in total trains on monday and the following tuesday")
plt.hist(delayed_diffs, alpha=0.5, label="difference in delayed trains on monday and the following tuesday")
plt.legend()
plt.show()