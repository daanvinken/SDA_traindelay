# plot showing a scatterplot between amount of stops made per day, and amount of delayed stops made per day
import matplotlib.pyplot as plt
import csv
import numpy as np

columns = [
    "date", "station", "trainnumber", "company",
    "traintype", "destination", "time", "delay", "canceled"
]

# Dictionary contains dates as keys and sets of trainnumbers as values
total_trains = {}
delayed_trains = {}

companies = [
    'R-net', 'U-OV', 'NS', 'Valleilijn', 'GVB', 'DB',
    'Railexpert', 'Arriva', 'Rail2U', 'Keolis', 'Railpromo',
    'Eurobahn', 'NMBS', 'Blauwnet', 'Abellio Ra', 'ABRN', 'Breng'
]

for i in companies:
    delayed_trains[i] = 0;

for i in companies:
    total_trains[i] = 0;

with open("../data/ALL_trains_2019_08_01_to_2019_11_01.csv") as vertrektijden:
    reader = csv.reader(vertrektijden, delimiter=",")

    for line in reader:
        company = line[columns.index("company")];

        if company not in companies:
            continue

        delay = line[columns.index("delay")]

        total_trains[company] = total_trains[company] + 1

        if int(delay) > 0:
            delayed_trains[company] = delayed_trains[company] + 1

# plt.scatter(total_trains.values(), delayed_trains.values(), alpha=0.1)
# plt.ylabel("Amount of delayed stops per day")
# plt.xlabel("Amount of stops per day")
# plt.show()

performance = [];

for i in delayed_trains:
    performance.append(delayed_trains[i] / total_trains[i])

y_pos = np.arange(len(companies))
# performance = delayed_trains.values()

plt.bar(y_pos, performance, align='center')
plt.xticks(y_pos, companies, rotation='vertical')
plt.tight_layout()

plt.show()

# print(companies, totals)
