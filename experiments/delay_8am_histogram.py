# histogram showing amount of delayed stops per weekday at 8am
import scipy.stats as st
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

        time = line[columns.index("time")]
        hour, _, _ = time.split(":")

        if (hour != "08"): continue

        delay = line[columns.index("delay")]

        if int(delay) > 0:
            if date not in delayed_trains:
                delayed_trains[date] = 1
            else:
                delayed_trains[date] = delayed_trains[date] + 1

delayed = list(delayed_trains.values())

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

xs = range(0, 2500)
ys = st.norm.pdf(xs, loc=delayed_mean, scale=delayed_std)

plt.hist(delayed, 20, density=True, label="Amount of delayed stops at 8am per weekday")
plt.plot(xs, ys, label="normal distribution with calculated delayed mean and stddev from sample")

plt.legend()
plt.show()
