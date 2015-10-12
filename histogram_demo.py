'''
histograms
Roger Milton, 12th October 2015
'''

import matplotlib.pyplot as plt
import numpy as np
from random import randint

# create n random numers up to upper

n=25
upper=200

rand_list = [-1]*n

for i in range(n):
    rand_list[i] = randint(0,upper)

# create a range of bins to put data in

my_bins=[0,7,14,30,90,120]
my_bins.append(max(rand_list))

hist, bin_edges = np.histogram(rand_list, bins=my_bins)

# print out the list, bins, and distribution

print('\nrand list is:',rand_list)
print('\nbins are:',bin_edges)
print('\nhist is:', hist)

# create labels for each pair of bin edges

labs = []
for i in range(len(bin_edges)-1):
    if hist[i] > 0:
        labs.append('['+str(bin_edges[i])+' - '+str(bin_edges[i+1])+')')
    else:
        labs.append('')

# example how this could be put on a pie chart

plt.figure()
plt.pie(hist, labels=labs)
plt.show()
