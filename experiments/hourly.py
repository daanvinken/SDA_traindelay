# plot showing amount of (delayed) trains per hour of the day
import matplotlib.pyplot as plt
import csv
import datetime

columns = [
    "date", "station", "trainnumber", "company",
    "traintype", "destination", "time", "delay", "canceled"
]

# Dictionary contains dates as keys and sets of trainnumbers as values
total_trains = {"00": 0, "01": 0, "02": 0, "03": 0, "04": 0, "05": 0, "06": 0, "07": 0, "08": 0, "09": 0, "10": 0, "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0, "18": 0, "19": 0, "20": 0, "21": 0, "22": 0, "23": 0, }
delayed_trains = {"00": 0, "01": 0, "02": 0, "03": 0, "04": 0, "05": 0, "06": 0, "07": 0, "08": 0, "09": 0, "10": 0, "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0, "18": 0, "19": 0, "20": 0, "21": 0, "22": 0, "23": 0, }


with open("../data/vertrektijden.csv") as vertrektijden:
    reader = csv.reader(vertrektijden, delimiter=",")

    for line in reader:

        time = line[columns.index("time")]
        hour, _, _ = time.split(":")

        delay = line[columns.index("delay")]

        if hour not in total_trains:
            total_trains[hour] = 1
        else:
            total_trains[hour] = total_trains[hour] + 1

        if int(delay) > 0:
            if hour not in delayed_trains:
                delayed_trains[hour] = 1
            else:
                delayed_trains[hour] = delayed_trains[hour] + 1

plt.plot(*zip(*total_trains.items()), label="total trains")
plt.plot(*zip(*delayed_trains.items()), label="total delays")
plt.xlabel("hours of the day")
plt.ylabel("amount")
plt.legend()
plt.show()
