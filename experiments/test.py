

powerlaw = lambda x, amp, index: amp * (x**index)

# libraries we need
import sys
import getopt
import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy
import time
import pylab as plt
from scipy import optimize

# get arguments
argumentList = sys.argv[1:]

# define allowed arguments
unixOptions = ""
gnuOptions = ["max_delay=", "bins="]

# check that we get commands in the right format
try:
    arguments, _ = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
    print(str(err))
    exit()

#default values
max_delay = 50
bins = 50

for arg, value in arguments:
    if arg == '--max_delay':
        print("setting max delay time to %s" % (value))
        max_delay = int(value)
    if arg == '--bins':
        print("setting bins to %s" % (value))
        bins = int(value)

delayList = []

# we always use the same source file
with open('../data/delay.csv') as source_file:
    reader = csv.reader(source_file, delimiter=",")
    for row in reader:
            # write to list
        vertraging = int(row[7])
        cancelled = int(row[8])
        if (vertraging <= max_delay):
            delayList.append(vertraging)

something = plt.hist(delayList, bins=bins)
for i in range(len(something[0])):
    print(something[0][i])
print("xxxxxxxxxxxx")
for i in range(len(something[1])):
    print(something[1][i])


# plt.show()

yerr = 2
xdata = something[1][:-1]
ydata = something[0]

logx = np.log10(xdata)
logy = np.log10(ydata)
logyerr = yerr / ydata

# define our (line) fitting function
fitfunc = lambda p, x: p[0] + p[1] * x
errfunc = lambda p, x, y, err: (y - fitfunc(p, x)) / err

pinit = [1.0, -1.0]
out = optimize.leastsq(errfunc, pinit,
                       args=(logx, logy, logyerr), full_output=1)

pfinal = out[0] 
covar = out[1]
print(pfinal)
print(covar)

index = pfinal[1]
amp = 10.0**pfinal[0]

indexErr = np.sqrt( covar[1][1] )
ampErr = np.sqrt( covar[0][0] ) * amp

##########
# Plotting data
##########

plt.clf()
plt.yscale("log")
plt.xscale("log")
plt.xlabel("Delay in minutes (excluding cancelled trains)")
plt.ylabel("Occurences (log)")
plt.hist(delayList, bins=49)
plt.plot(xdata, powerlaw(xdata, amp, index))     # Fit
plt.text(5, 6.5, 'Ampli = %5.2f +/- %5.2f' % (amp, ampErr))
plt.title('Best Fit Power Law')
plt.show()

# plt.subplot(2, 1, 2)
# plt.loglog(xdata, powerlaw(xdata, amp, index))
# plt.errorbar(xdata, ydata, yerr=yerr, fmt='k.')  # Data
# plt.xlabel('X (log scale)')
# plt.ylabel('Y (log scale)')
# plt.xlim(1.0, 11)
# plt.show()