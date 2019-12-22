import scipy.stats as st
import matplotlib.pyplot as plt
import csv
import datetime
import numpy as np

# Provides for intuitive way of getting the right column from csv
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

        # Limit delay to at most 30 minutes, since after this
        # it is unlikely that a train will not be canceled.
        if delay >= 1 and delay <= 30:
            delays.append(delay)

# Get exponential distributions parameters corresponding to best-fitting
# exponential curve.
scipy_params = st.expon.fit(delays, floc=0)

# Run a Kolmogorov-Smirnov test using SciPy and get p-value
p = st.kstest(delays, 'expon', scipy_params)[1]

x = np.linspace(1, 30, 100)

f = plt.figure()

plt.xlabel("Minutes delay")
plt.ylabel("Frequencies (normalized)")
plt.title("Time delay follows exponential distribution with p-value {} (rejection)".format(p))
plt.legend()

plt.hist(delays, bins=30, label="Observations", density=True)

# Plot probability distribution for every minute.
plt.plot(x, st.expon(*scipy_params).pdf(x), label="scipy expon fit")

plt.show()
f.savefig('../results/delay_time_distribution.png', bbox_inches='tight')
