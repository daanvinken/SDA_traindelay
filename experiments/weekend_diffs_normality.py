import scipy.stats as st
import matplotlib.pyplot as plt
import csv
import datetime

columns = [
    "date", "station", "trainnumber", "company",
    "traintype", "destination", "time", "delay", "cancelled"
]

# Dictionary contains dates as keys and occurences as values
total_trains = {}

with open("../data/vertrektijden.csv") as vertrektijden:
    reader = csv.reader(vertrektijden, delimiter=",")

    for line in reader:

        date = line[columns.index("date")]
        delay = line[columns.index("delay")]
        year, month, day = date.split("-")
        weekday = datetime.date(int(year), int(month), int(day)).weekday()

        # filtering out weekdays
        if (weekday < 5): continue

        if date not in total_trains:
            total_trains[date] = 1
        else:
            total_trains[date] = total_trains[date] + 1

total_sat = []
total_sun = []
total_diffs = []

for key in total_trains.keys():
    year, month, day = key.split("-")
    weekday = datetime.date(int(year), int(month), int(day)).weekday()

    if (weekday == 5):
        total_sat.append(total_trains[key])
    else:
        total_sun.append(total_trains[key])       

for i in range(len(total_sat)):
    total_diffs.append(total_sat[i] - total_sun[i])

mean_diffs = sum(total_diffs)/len(total_diffs)

def stddev(sample, mean):
    diffs = []
    for num in sample:
        diffs.append((num - mean)**2)

    variance = sum(diffs)/len(diffs)
    return variance**0.5

std_diffs = stddev(total_diffs, mean_diffs)
print("calculated mean is %s" % (mean_diffs))
print("calculated standard deviation is %s" % (std_diffs))

_, p = st.kstest(total_diffs, 'norm', (mean_diffs, std_diffs))
_, p2 = st.kstest(total_diffs, 'norm', (5000, 500))
print("calculated p-value from normal distribution with calculated mean and standard deviation is %s (no rejection)" % (p))
print("calculated p-value from normal distribution with mean = 5000 and standard deviation = 500 is %s (no rejection)" % (p2))

xs = range(3500, 6500)
ys = st.norm.pdf(xs, loc=mean_diffs, scale=std_diffs)
ys2 = st.norm.pdf(xs, loc=5000, scale=500)

plt.hist(total_diffs, density=True, alpha=0.5, label="difference in total trains on saturday and the following sunday")
plt.plot(xs, ys, alpha=0.5, label="normal distribution with calculated mean and stddev from sample")
plt.plot(xs, ys2, alpha=0.5, label="normal distribution with mean = 5000 and stddev = 500")
plt.legend()
plt.show()