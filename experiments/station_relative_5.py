# histogram showing amount of delays divided by stops per station
import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt
import csv
import datetime

columns = [
    "date", "station", "trainnumber", "company",
    "traintype", "destination", "time", "delay", "canceled"
]

# Dictionary contains stations as keys and occurences as values
total_trains = {}
delayed_trains = {}

with open("../data/vertrektijden.csv") as vertrektijden:
    reader = csv.reader(vertrektijden, delimiter=",")

    for line in reader:

        station = line[columns.index("station")]

        delay = line[columns.index("delay")]

        if station not in total_trains:
            total_trains[station] = 1
        else:
            total_trains[station] = total_trains[station] + 1

        if int(delay) > 4:
            if station not in delayed_trains:
                delayed_trains[station] = 1
            else:
                delayed_trains[station] = delayed_trains[station] + 1

relative_delays = []
for key in total_trains.keys():
    relative_delays.append(delayed_trains.get(key, 0) / total_trains[key])

relative_mean = sum(relative_delays)/len(relative_delays)

def stddev(sample, mean):
    diffs = []
    for num in sample:
        diffs.append((num - mean)**2)

    variance = sum(diffs)/len(diffs)
    return variance**0.5

relative_std = stddev(relative_delays, relative_mean)
print("calculated delayed mean is %s" % (relative_mean))
print("calculated delayed standard deviation is %s" % (relative_std))

_, p = st.kstest(relative_delays, 'norm', (relative_mean, relative_std))
print("calculated p-value from normal distribution with calculated delayed mean and standard deviation is %s (no rejection)" % (p))

xs = np.arange(-0.04, 0.16, 0.001)
ys = st.norm.pdf(xs, loc=relative_mean, scale=relative_std)

plt.hist(relative_delays, 20, density=True, label="percentage of trains delayed at least 5 minutes per station")
plt.plot(xs, ys, label="normal distribution with calculated delayed mean and stddev from sample")
plt.legend()
plt.show()