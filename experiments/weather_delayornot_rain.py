#plot showing amount of stops and delays per date (total), filtering out weekends for smoother lines
import matplotlib.pyplot as plt
import csv
import datetime

columns = [
    "date", "station", "trainnumber", "company",
    "traintype", "destination", "time", "delay", "cancelled"
]


#ive added some extra outliers, but i don't know why they exist yet.
# So maybe they should be included.
obsolete_dates = ['2018-09-03', '2018-12-25', '2018-12-26','2018-12-31', '2019-01-01',
'2019-04-19', '2019-04-21', '2019-04-22','2019-05-05','2019-05-28', '2019-05-30',
 '2019-06-09','2019-06-10', '2019-11-26']
other_outliers = ['2018-09-12', '2018-10-09', '2018-12-03', '2019-02-13', '2019-06-25',
 '2019-08-14', '2019-08-15', '2019-08-16', '2019-08-19', '2019-08-20', '2019-08-21',
  '2019-09-02']
obsolete_dates_w = ['20180903', '20181225', '20181226','20181231', '20190101',
'20190419', '20190421', '20190422','20190505','20190528', '20190530',
 '20190609','20190610', '20191126',
 '20180912', '20181009', '20181203', '20190213', '20190625',
 '20190814', '20190815', '20190816', '20190819', '20190820', '20190821',
  '20190902']

# Dictionary contains dates as keys and occurences as values
total_trains = {}
total_delayed_trains = {}

with open("../data/vertrektijden.csv") as vertrektijden:
    reader = csv.reader(vertrektijden, delimiter=";")

    for line in reader:

        date = line[columns.index("date")]
        if (str(date) in obsolete_dates) or (date in other_outliers) : continue
        delay = line[columns.index("delay")]
        year, month, day = date.split("-")
        weekday = datetime.date(int(year), int(month), int(day)).weekday()

        # filtering out weekends
        if (weekday >= 5): continue
        if int(delay) == 0:
            if date in total_trains:
                total_trains[date] = total_trains[date] + 1
            else:
                total_trains[date] = 1
        else:
            if date in total_delayed_trains:
                total_delayed_trains[date] = total_delayed_trains[date] + 1
            else:
                total_delayed_trains[date] = 1

rainlist = []
with open("../data/neerslag.txt") as neerslag:
    reader = csv.reader(neerslag, delimiter=",")
    for line in reader:
        date = str(line[1])
        if ((str(date) in obsolete_dates_w)): continue
        weekday = datetime.date(int(line[1][:4]), int(line[1][4:6]), int(line[1][6:8])).weekday()
        rain = int(line[2])
        if (weekday >=5): continue
        rainlist.append(int(rain))
print("lengths " + str(len(total_trains)))
print("lengthss " + str(len(rainlist)))

percentage_delayed_per_day = []
for date in total_trains.keys():
    factor = (total_delayed_trains[str(date)] / (total_delayed_trains[str(date)] + total_trains[str(date)]))*100
    percentage_delayed_per_day.append(factor)

print(len(percentage_delayed_per_day))
print(len(rainlist))


fig, ax1 = plt.subplots()
ax1.plot(rainlist, 'b-')
ax1.tick_params('y', colors='b')
ax2 = ax1.twinx()

ax2.tick_params('y', colors='r')
ax2.plot(*zip(*sorted(total_trains.items())), label="total trains", color='r')
fig.tight_layout()
plt.title("Blue line, rain in mm on a day. Red line number of delayed trains on a day")
plt.show()

