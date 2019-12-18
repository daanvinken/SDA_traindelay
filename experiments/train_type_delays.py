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

types = [
    'Extra trein', 'Stopbus i.p.v. trein', 'Snelbus i.p.v. trein',
    'Sprinter', 'Intercity direct', 'Intercity', 'Bus', 'Speciale Trein',
    'Int. Trein', 'Eurostar', 'Thalys', 'ICE International'
]

for i in types:
    delayed_trains[i] = 0;

for i in types:
    total_trains[i] = 0;

with open("../data/NS_trains_2019_08_01_to_2019_11_01.csv") as vertrektijden:
    reader = csv.reader(vertrektijden, delimiter=",")

    for line in reader:
        type = line[columns.index("traintype")];
        delay = line[columns.index("delay")]

        total_trains[type] = total_trains[type] + 1

        if int(delay) > 0:
            delayed_trains[type] = delayed_trains[type] + 1

# plt.scatter(total_trains.values(), delayed_trains.values(), alpha=0.1)
# plt.ylabel("Amount of delayed stops per day")
# plt.xlabel("Amount of stops per day")
# plt.show()

performance = [];

for i in delayed_trains:
    performance.append(delayed_trains[i] / total_trains[i])

y_pos = np.arange(len(types))

f = plt.figure()

plt.bar(y_pos, performance, align='center')
plt.xticks(y_pos, types, rotation='vertical')
plt.tight_layout()

plt.show()

f.savefig('../results/train_type_delays.png', bbox_inches='tight')
