#!/usr/bin/python
# Deepak Ramanath

import os
import sys
import pandas as pd
import numpy as np
import random
import collections
import matplotlib.pyplot as plt

# Function
def tempFunction(ld):
	i = 0
	while i < ld:
		i = i + 1
		temp = random.randrange(20, 40, 2)
		tempDays.append(temp)
	return temp

# Some essential lists
tempDays = []
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
lenDays =  len(days)

# Calling the temperature function to generate random temperatures
tempFunction(lenDays)

# Creating a ordered dictionary
tempData = collections.OrderedDict(zip(days, tempDays))
print tempData

# Creating a Pandas Series
data = pd.Series(tempData)
print type(data)
print type(data.values)

# Specifying the names to the Pandas Series
data.name = 'Temperature'
data.index.name = 'Weekday'
print data

# Calculating some statistics of temperature
print "Maximum weekly temperature:", data.max()
print "Minumim weekly temperature:", data.min()
print "Weekly mean temperature:", data.median()

# Plotting the temperature variation

plt.plot(data, marker='o', linestyle='-', color='r')
plt.xlabel('Days [Index]')
plt.ylabel('Temperature [C]')
plt.title('Temperature variation over a period of one week')
plt.show()
