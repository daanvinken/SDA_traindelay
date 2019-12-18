import scipy.stats as st
import matplotlib.pyplot as plt
import csv
import datetime
import numpy as np

columns = [
    "date", "station", "trainnumber", "company",
    "traintype", "destination", "time", "delay", "canceled"
]

obsolete_dates = [
    "2018-09-03", "2018-12-25", "2018-12-26","2018-12-31", "2019-01-01",
    "2019-04-19", "2019-04-21", "2019-04-22","2019-05-05","2019-05-28",
    "2019-05-30", "2019-06-09","2019-06-10", "2019-11-26"
]

# Dictionary contains dates as keys and sets of trainnumbers as values
delayed_trains = {}
canceled_trains = {}

# with open("../data/ALL_trains_2019_08_01_to_2019_11_01.csv") as vertrektijden:
with open("../data/vertrektijden.csv") as vertrektijden:
    reader = csv.reader(vertrektijden, delimiter=",")

    for line in reader:
        date = line[columns.index("date")]

        if date in obsolete_dates:
            continue

        year, month, day = date.split("-")
        weekday = datetime.date(int(year), int(month), int(day)).weekday()

        # filtering out weekends
        if (weekday >= 5): continue

        delay = line[columns.index("delay")]
        canceled = line[columns.index("canceled")]

        if date not in delayed_trains:
            delayed_trains[date] = 0

        if date not in canceled_trains:
            canceled_trains[date] = 0

        # Number of stops with delay:
        if int(delay) >= 1:
            delayed_trains[date] += 1

        # Number of canceled trains
        if int(canceled) == 1:
            canceled_trains[date] += 1

delays = {}

# Iterate over all dates (canceled and delayed have same dates)
for date in delayed_trains:
    delay_frequency = delayed_trains[date]
    canceled_frequency = canceled_trains[date]

    # Found first occurence of specific delay frequency
    if delay_frequency not in delays:
        delays[delay_frequency] = (1, canceled_frequency)

    # Take average of current and previously found canceled trains
    else:
        count = delays[delay_frequency][0] + 1
        freqs = delays[delay_frequency][1]
        avg = (freqs + canceled_frequency) / count
        delays[delay_frequency] = (count, avg)

# sort = {}

# Sort delay frequencies for better plotting
# for i in sorted(list(delays.keys())):
#     sort[i] = delays[i]

xs = list(delays.keys())
ys = [y[1] for y in delays.values()]

plt.scatter(xs, ys, marker='.')

# solve for a and b
def best_fit(X, Y):

    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X) # or len(Y)

    numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2

    b = numer / denum
    a = ybar - b * xbar

    print('best fit line:\ny = {:.2f} + {:.2f}x'.format(a, b))

    return a, b

# plt.plot(np.unique(xs), np.poly1d(np.polyfit(xs, ys, 1))(np.unique(xs)), 'r')
# plt.hist(xs)
plt.xlabel("Number of delays")
plt.ylabel("Number of canceled trains")

a, b = best_fit(xs, ys)


yfit = [a + b * xi for xi in xs]
plt.plot(xs, yfit, 'r')
# plt.show()
plt.savefig('../results/canceled_per_delay2.png', bbox_inches='tight')
