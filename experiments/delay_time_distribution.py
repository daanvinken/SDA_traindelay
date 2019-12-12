import seaborn as sns
import matplotlib.pyplot as plt
import csv
import numpy as np

columns = [
    "date", "station", "trainnumber", "company",
    "traintype", "destination", "time", "delay", "canceled"
]

delays = []

gt = 0

with open("../data/NS_delayed_trains_2019_08_01_to_2019_11_01.csv") as vertrektijden:
    reader = csv.reader(vertrektijden, delimiter=",")

    for line in reader:
        delay = int(line[columns.index("delay")])

        # if delay >= 60:
            # gt += 1

        if delay < 120:
            delays.append(delay);

plt.hist(delays, bins=30)
plt.yscale('log', nonposy='clip')
plt.show()

sns.distplot(delays)
plt.yscale('log', nonposy='clip')
plt.show()

print(gt)
