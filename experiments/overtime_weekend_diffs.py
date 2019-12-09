#histogram showing difference of stops and delays per date (total), filtering out weekdays for smoother lines
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

        # filtering out weekdays
        if (weekday < 5): continue

        if date not in total_trains:
            total_trains[date] = 1
            delayed_trains[date] = 0
        else:
            total_trains[date] = total_trains[date] + 1

        if int(delay) > 0:
            delayed_trains[date] = delayed_trains[date] + 1

total_sat = []
total_sun = []
total_diffs = []
delayed_sat = []
delayed_sun = []
delayed_diffs = []

for key in total_trains.keys():
    year, month, day = key.split("-")
    weekday = datetime.date(int(year), int(month), int(day)).weekday()

    if (weekday == 5):
        total_sat.append(total_trains[key])
    else:
        total_sun.append(total_trains[key])       

for i in range(len(total_sat)):
    total_diffs.append(total_sat[i] - total_sun[i])

for key in delayed_trains.keys():
    year, month, day = key.split("-")
    weekday = datetime.date(int(year), int(month), int(day)).weekday()

    if (weekday == 5):
        delayed_sat.append(delayed_trains[key])
    else:
        delayed_sun.append(delayed_trains[key])       

for i in range(len(delayed_sat)):
    delayed_diffs.append(delayed_sat[i] - delayed_sun[i])

plt.hist(total_diffs, alpha=0.5, label="difference in total trains on saturday and the following sunday")
plt.hist(delayed_diffs, alpha=0.5, label="difference in delayed trains on saturday and the following sunday")
plt.legend()
plt.show()