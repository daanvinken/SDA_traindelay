#plot showing amount of stops and delays per date (total), filtering out weekdays for smoother lines
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

total_sat = {}
total_sun = {}
delayed_sat = {}
delayed_sun = {}

for key in total_trains.keys():
    year, month, day = key.split("-")
    weekday = datetime.date(int(year), int(month), int(day)).weekday()

    if (weekday == 5):
        total_sat[key] = total_trains[key]
    else:
        total_sun[key] = total_trains[key]        

for key in delayed_trains.keys():
    year, month, day = key.split("-")
    weekday = datetime.date(int(year), int(month), int(day)).weekday()

    if (weekday == 5):
        delayed_sat[key] = delayed_trains[key]
    else:
        delayed_sun[key] = delayed_trains[key]  

plt.plot(range(len(total_sat.keys())), list(total_sat.values()), label="total saturday")
plt.plot(range(len(total_sun.keys())), list(total_sun.values()), label="total sunday")
plt.plot(range(len(delayed_sat.keys())), list(delayed_sat.values()), label="delayed saturday")
plt.plot(range(len(delayed_sun.keys())), list(delayed_sun.values()), label="delayed sunday")
plt.legend()
plt.show()