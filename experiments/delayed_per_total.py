import matplotlib.pyplot as plt
import csv
import numpy as np

# Provides for intuitive way of getting the right column from csv
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

# Initialize number of delayed stops that were made by
# a vehicle from a company
for i in companies:
    delayed_trains[i] = 0;

# Initialize number of stops that were made by a vehicle
# from a company
for i in companies:
    total_trains[i] = 0;

with open("../data/vertrektijden.csv") as vertrektijden:
    reader = csv.reader(vertrektijden, delimiter=",")

    for line in reader:
        company = line[columns.index("company")];

        # Some companies occur so little that we do not want
        # list them in our graph.
        if company not in companies:
            continue

        delay = line[columns.index("delay")]

        total_trains[company] += 1

        if int(delay) > 0:
            delayed_trains[company] += 1

ratio = [];

# Get ratio of delayed stops versus total number of stops
for i in delayed_trains:
    ratio.append(delayed_trains[i] / total_trains[i])

y_pos = np.arange(len(companies))

f = plt.figure()

plt.bar(y_pos, ratio, align='center')
plt.xticks(y_pos, companies, rotation='vertical')
plt.xlabel("Companies")
plt.ylabel("Percentage delayed stops of total stops")

plt.tight_layout()

plt.show()

f.savefig('../results/delayed_per_total.png', bbox_inches='tight')
