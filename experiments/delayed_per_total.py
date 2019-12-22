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

with open("../data/vertrektijden.csv") as vertrektijden:
    reader = csv.reader(vertrektijden, delimiter=",")

    for line in reader:
        company = line[columns.index("company")];

        if company not in companies:
            continue

        delay = line[columns.index("delay")]

        total_trains[company] = total_trains[company] + 1

        if int(delay) > 0:
            delayed_trains[company] = delayed_trains[company] + 1

performance = [];

for i in delayed_trains:
    performance.append(delayed_trains[i] / total_trains[i])

y_pos = np.arange(len(companies))

f = plt.figure()

plt.bar(y_pos, performance, align='center')
plt.xticks(y_pos, companies, rotation='vertical')
plt.xlabel("Companies")
plt.ylabel("$\\dfrac{\\mathrm{delayed}}{\\mathrm{total}} \%$")
plt.tight_layout()

plt.show()

f.savefig('../results/delayed_per_total.png', bbox_inches='tight')

# print(companies, totals)
