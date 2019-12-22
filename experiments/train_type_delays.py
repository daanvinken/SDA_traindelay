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

# All carrier types the NS uses
types = [
    'Extra trein', 'Sprinter', 'Intercity direct', 'Intercity',
    'Speciale Trein', 'Int. Trein', 'Eurostar', 'Thalys', 'ICE International'
]

# Initialize number of delayed stops that were made by
# a carrier from NS
for i in types:
    delayed_trains[i] = 0;

# Initialize number of stops that were made by
# a carrier from NS
for i in types:
    total_trains[i] = 0;

with open("../data/ns_vertrektijden.csv") as vertrektijden:
    reader = csv.reader(vertrektijden, delimiter=",")

    for line in reader:
        type = line[columns.index("traintype")];
        delay = line[columns.index("delay")]

        # Some carries types occur so little that we do not want
        # list them in our plot.
        if type not in total_trains:
            continue

        total_trains[type] += 1

        if int(delay) > 0:
            delayed_trains[type] += 1

ratio = [];

# Get ratio of delayed stops versus total number of stops
for i in delayed_trains:
    ratio.append(delayed_trains[i] / total_trains[i])

y_pos = np.arange(len(types))

f = plt.figure()

plt.bar(y_pos, ratio, align='center')
plt.xticks(y_pos, types, rotation='vertical')
plt.xlabel("Companies")
plt.ylabel("Percentage delayed stops of total stops")

plt.tight_layout()

plt.show()

f.savefig('../results/train_type_delays.png', bbox_inches='tight')
