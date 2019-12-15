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

with open("../data/NS_delayed_trains_2019_08_01_to_2019_11_01.csv") as vertrektijden:
    reader = csv.reader(vertrektijden, delimiter=",")

    for line in reader:
        delay = int(line[columns.index("delay")])

        if delay <= 30:
            delays.append(delay)

scipy_params = st.expon.fit(delays, floc=0)

print(st.kstest(delays, 'expon', scipy_params)[1])
x = np.linspace(1, 30, 100)
plt.hist(delays, bins=15, label="Observations", density=True)
plt.plot(x, st.expon(*scipy_params).pdf(x), label="scipy expon fit")
plt.ylabel("Frequencies (normalized)")
plt.xlabel("Minutes delay")
plt.legend()
plt.show()

# plt.plot(list(data.keys()), list(data.values()))
# plt.show()
