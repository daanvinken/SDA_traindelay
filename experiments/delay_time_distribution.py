# histogram showing amount of delayed stops per weekday at 8am
import scipy.stats as st
import matplotlib.pyplot as plt
import csv
import datetime
from collections import OrderedDict
import numpy as np

columns = [
    "date", "station", "trainnumber", "company",
    "traintype", "destination", "time", "delay", "canceled"
]

# Dictionary contains dates as keys and sets of trainnumbers as values
delayed_trains = {}
delays = []

with open("../data/vertragingen.csv") as vertrektijden:
    reader = csv.reader(vertrektijden, delimiter=",")

    for line in reader:
        delay = int(line[columns.index("delay")])

        if delay <= 30:
            delays.append(delay)

delays = np.array(delays)

p = 1 / float(np.mean(delays))
k = np.arange(1, delays.max() + 1)

f = plt.figure()

freqs, _, _ = plt.hist(delays, bins=30, label="Observations")
plt.plot(k, st.geom.pmf(k, p) * len(delays), 'r', label="Geometric distribution")

p_value = st.chisquare(freqs, st.geom.pmf(k, p) * len(delays))[1]

plt.title("Fit geometric distribution on data, p-value {} (Rejection)".format(p_value))
plt.ylabel("Frequencies")
plt.xlabel("Minutes delay")
plt.legend()

plt.show()
f.savefig('../results/delay_time_distribution.png', bbox_inches='tight')


# print(freqs)
# print(st.geom.pmf(k, p) * len(delays))

# print()

# plt.hist(delays, bins=30, label="Observations", density=True)
# plt.plot(k, st.geom.pmf(k, p), '.r')
# plt.show()
# plt.plot(x, st.expon(*scipy_params).pdf(x), label="scipy expon fit")
# plt.title("p-value {} (rejection), location: {}, scale: {}".format(p, *scipy_params))
# plt.legend()
# # plt.show()
# plt.savefig('../results/delay_time_distribution.png', bbox_inches='tight')
#
# # plt.plot(list(data.keys()), list(data.values()))
# # plt.show()
