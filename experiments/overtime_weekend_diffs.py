#histogram showing difference of stops and delays per date (total), filtering out weekdays for smoother lines
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
delayed_trains = {}

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
            delayed_trains[date] = 0
        else:
            total_trains[date] = total_trains[date] + 1

        if int(delay) > 0:
            delayed_trains[date] = delayed_trains[date] + 1

total_sat = []
total_sun = []
total_diffs = []
delayed_sat = []
delayed_sun = []
delayed_diffs = []

for key in total_trains.keys():
    year, month, day = key.split("-")
    weekday = datetime.date(int(year), int(month), int(day)).weekday()

    if (weekday == 5):
        total_sat.append(total_trains[key])
    else:
        total_sun.append(total_trains[key])       

for i in range(len(total_sat)):
    total_diffs.append(total_sat[i] - total_sun[i])

for key in delayed_trains.keys():
    year, month, day = key.split("-")
    weekday = datetime.date(int(year), int(month), int(day)).weekday()

    if (weekday == 5):
        delayed_sat.append(delayed_trains[key])
    else:
        delayed_sun.append(delayed_trains[key])       

for i in range(len(delayed_sat)):
    delayed_diffs.append(delayed_sat[i] - delayed_sun[i])

total_mean_diffs = sum(total_diffs)/len(total_diffs)
delayed_mean_diffs = sum(delayed_diffs)/len(delayed_diffs)

def stddev(sample, mean):
    diffs = []
    for num in sample:
        diffs.append((num - mean)**2)

    variance = sum(diffs)/len(diffs)
    return variance**0.5

total_std_diffs = stddev(total_diffs, total_mean_diffs)
print("calculated total mean is %s" % (total_mean_diffs))
print("calculated total standard deviation is %s" % (total_std_diffs))
delayed_std_diffs = stddev(delayed_diffs, delayed_mean_diffs)
print("calculated delayed mean is %s" % (delayed_mean_diffs))
print("calculated delayed standard deviation is %s" % (delayed_std_diffs))

_, total_p = st.kstest(total_diffs, 'norm', (total_mean_diffs, total_std_diffs))
_, delayed_p = st.kstest(delayed_diffs, 'norm', (delayed_mean_diffs, delayed_std_diffs))
print("calculated p-value from normal distribution with calculated total mean and standard deviation is %s (no rejection)" % (total_p))
print("calculated p-value from normal distribution with calculated delayed mean and standard deviation is %s (no rejection)" % (delayed_p))

total_xs = range(3500,6500)
delayed_xs = range(-1500, 6500)

total_ys = st.norm.pdf(total_xs, loc=total_mean_diffs, scale=total_std_diffs)
delayed_ys = st.norm.pdf(delayed_xs, loc=delayed_mean_diffs, scale=delayed_std_diffs)

plt.hist(total_diffs, alpha=0.5, density=True, label="difference in total trains on saturday and the following sunday")
plt.hist(delayed_diffs, alpha=0.5, density=True, label="difference in delayed trains on saturday and the following sunday")
plt.plot(total_xs, total_ys, alpha=0.5, label="normal distribution with calculated total mean and stddev from sample")
plt.plot(delayed_xs, delayed_ys, alpha=0.5, label="normal distribution with calculated delayed mean and stddev from sample")

plt.legend()
plt.show()