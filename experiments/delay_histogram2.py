# histogram showing amount of delayed stops per weekday
import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt
import csv
import datetime

columns = [
    "date", "station", "trainnumber", "company",
    "traintype", "destination", "time", "delay", "canceled"
]

obsolete_dates = [
    '2018-09-03', '2018-12-25', '2018-12-26', '2018-12-31',
    '2019-01-01', '2019-04-19', '2019-04-21', '2019-04-22',
    '2019-05-05', '2019-05-28', '2019-05-30', '2019-06-09',
    '2019-06-10', '2019-11-26'
]

# Dictionary contains dates as keys and sets of trainnumbers as values
delayed_trains = {}

with open("../data/vertrektijden.csv") as vertrektijden:
    reader = csv.reader(vertrektijden, delimiter=",")

    for line in reader:

        date = line[columns.index("date")]
        year, month, day = date.split("-")
        weekday = datetime.date(int(year), int(month), int(day)).weekday()

        if (date in obsolete_dates) : continue

        # filtering out weekends
        if (weekday >= 5): continue

        delay = line[columns.index("delay")]

        if int(delay) > 0:
            if date not in delayed_trains:
                delayed_trains[date] = 1
            else:
                delayed_trains[date] = delayed_trains[date] + 1

delayed_log = list(delayed_trains.values())
# calculate (ln(delayed))
print("since we expect the distribution of X to be lognormal, that means ln(X) must be normal, and we will calculate the p-value for that instead")
delayed = [np.log(x) for x in delayed_log]

delayed_mean = sum(delayed)/len(delayed)

def stddev(sample, mean):
    diffs = []
    for num in sample:
        diffs.append((num - mean)**2)

    variance = sum(diffs)/len(diffs)
    return variance**0.5

delayed_std = stddev(delayed, delayed_mean)
print("calculated delayed mean is %s" % (delayed_mean))
print("calculated delayed standard deviation is %s" % (delayed_std))

_, p = st.kstest(delayed, 'norm', (delayed_mean, delayed_std))
print("calculated p-value from normal distribution with calculated delayed mean and standard deviation is %s (no rejection)" % (p))

plt.hist(delayed_log, 25, label="Amount of delayed stops per weekday")
plt.legend()
plt.show()
