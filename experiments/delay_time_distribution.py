# histogram showing amount of delayed stops per weekday at 8am
import scipy.stats as st
import matplotlib.pyplot as plt
import csv
import datetime
import numpy as np

columns = [
    "date", "station", "trainnumber", "company",
    "traintype", "destination", "time", "delay", "canceled"
]

# Dictionary contains dates as keys and sets of trainnumbers as values
delayed_trains = {}
delays = []

with open("../data/vertrektijden.csv") as vertrektijden:
    reader = csv.reader(vertrektijden, delimiter=",")

    for line in reader:
        delay = int(line[columns.index("delay")])

        if delay >= 1 and delay <= 30:
            delays.append(delay)

scipy_params = st.expon.fit(delays, floc=0)

p = st.kstest(delays, 'expon', scipy_params)[1]
x = np.linspace(1, 30, 100)

f = plt.figure()

plt.hist(delays, bins=30, label="Observations", density=True)
plt.plot(x, st.expon(*scipy_params).pdf(x), label="scipy expon fit")
plt.ylabel("Frequencies (normalized)")
plt.xlabel("Minutes delay")
plt.title("time delay follows exponential distribution with p-value {} (rejection)".format(p))
plt.legend()

f.savefig('../results/delay_time_distribution.png', bbox_inches='tight')

plt.show()


# plt.plot(list(data.keys()), list(data.values()))
# plt.show()
