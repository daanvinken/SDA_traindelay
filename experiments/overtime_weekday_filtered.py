#plot showing amount of stops and delays per date (total), filtering out weekends and certain dates (such as Christmas) for smoother lines
import matplotlib.pyplot as plt
import csv
import datetime

columns = [
    "date", "station", "trainnumber", "company",
    "traintype", "destination", "time", "delay", "cancelled"
]

obsolete_dates = [
    '2018-09-03', '2018-12-25', '2018-12-26', '2018-12-31',
    '2019-01-01', '2019-04-19', '2019-04-21', '2019-04-22',
    '2019-05-05', '2019-05-28', '2019-05-30', '2019-06-09',
    '2019-06-10', '2019-11-26'
]

# Dictionary contains dates as keys and occurences as values
total_trains = {}
delayed_trains_1 = {}
delayed_trains_10 = {}
cancelled_trains = {}

with open("../data/vertrektijden.csv") as vertrektijden:
    reader = csv.reader(vertrektijden, delimiter=",")

    for line in reader:

        date = line[columns.index("date")]

        if (date in obsolete_dates): continue

        delay = line[columns.index("delay")]
        year, month, day = date.split("-")
        weekday = datetime.date(int(year), int(month), int(day)).weekday()
        cancelled = line[columns.index("cancelled")]

        # filtering out weekends
        if (weekday >= 5): continue

        if date not in total_trains:
            total_trains[date] = 1
            delayed_trains_1[date] = 0
            delayed_trains_10[date] = 0
            cancelled_trains[date] = 0
        else:
            total_trains[date] = total_trains[date] + 1

        if int(delay) > 0:
            delayed_trains_1[date] = delayed_trains_1[date] + 1

        if int(delay) > 9:
            delayed_trains_10[date] = delayed_trains_10[date] + 1

        if int(cancelled) == 1:
            cancelled_trains[date] = cancelled_trains[date] + 1

plt.plot(*zip(*sorted(total_trains.items())), label="total trains")
plt.plot(*zip(*sorted(delayed_trains_1.items())), label="at least 1 minute delayed")
plt.plot(*zip(*sorted(delayed_trains_10.items())), label="at least 10 minutes delayed")
plt.plot(*zip(*sorted(cancelled_trains.items())), label="cancelled trains")
plt.legend()
plt.show()
