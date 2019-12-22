#bins by default on 51 for max 50 minutes delay (one bar per minute)

# libraries we need
import sys
import getopt
import csv
import matplotlib.pyplot as plt

# get arguments
argumentList = sys.argv[1:]

# define allowed arguments
unixOptions = ""
gnuOptions = ["bins="]

# check that we get commands in the right format
try:
    arguments, _ = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
    print(str(err))
    exit()

#default values
max_delay = 800
bins = 100

for arg, value in arguments:
    if arg == '--bins':
        print("setting bins to %s" % (value))
        bins = int(value)


total_days_delay_list = []
#List with week days
week_days= ['Monday', 'Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']

# we always use the same source file
for day in week_days:
    days_delay_list = []
    with open('../data/delay.csv') as source_file:
        reader = csv.reader(source_file, delimiter=",")
        current_date = reader.__next__()[0]
        delay_counter=0
        for row in reader:
            print(row)            #Check for matching weekday
            if str(row[9]) == str(day):
                #check for current date (same day)``
                if str(current_date) == str(row[0]):
                    vertraging = int(row[7])
                    delay_counter += int(vertraging)
                else:
                    days_delay_list.append(delay_counter)
                    delay_counter = 0
                    current_date = reader.__next__()[0]
    total_days_delay_list.append(days_delay_list)
    print(days_delay_list)



fig, axs = plt.subplots(4, 2, sharex='col', sharey='row',
                        gridspec_kw={'hspace': 0, 'wspace': 0})
(ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8) = axs
fig.suptitle("{left to right} 'Monday', 'Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday'\n Total delay per day from all data.")
ax1.hist(total_days_delay_list[0],bins=bins)
ax2.hist(total_days_delay_list[1], bins=bins)
ax3.hist(total_days_delay_list[2], bins=bins)
ax4.hist(total_days_delay_list[3], bins=bins)
ax5.hist(total_days_delay_list[4], bins=bins)
ax6.hist(total_days_delay_list[5], bins=bins)
ax7.hist(total_days_delay_list[6], bins=bins)

for ax in axs.flat:
    ax.label_outer()
plt.show()

