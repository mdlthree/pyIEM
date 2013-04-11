from pandas import Series, DataFrame
import pandas as pd
df = pd.read_csv('scGameDemand.csv')
del df['day']

# import modules, read in the csv file and delete the column 'day' as the DataFrame index is the same here

df.plot(figsize=(12,8))
# plot the basic figure
# plot arguments 'figsize(12,8)' used to create a bigger graph
# I think options can be set at the beginning for a session so arguments are set once, I have not done that here

f = lambda x: x.sum()
df['rowsum'] = df.apply(f,axis=1)
# through the use of 'lambda' functions, a new column is created that is the sum of
#   demand of each region on a single day

df.plot(figsize=(12,16), subplots=True)

df.cumsum().plot(figsize=(12,8), xlim=[0,1460])
# with the cumsum series we could design several solutions to the production problem
#   such as a chase plan or find the miniumum capacity needed to satisfy the steepest demand

df[['Tyran', 'Fardo', 'Entworpe']].cumsum().plot(figsize=(12,8), xlim=[600,1460])
# what Tyran, Fardo and Entworpe cumulative sum curves look like when the scale is not dominated
#   by the other regions
# plot arguments 'xlim' used to display data after day 600

# Lets try and find the minimum capacity needed to fullfil demand for all 5 regions
#   after day 730

minCap = df['rowsum'][730:].cumsum()
# slice out the last 730 days and apply the cumulative sum function

# created a new dataframe from the total column and applied a cumulative function

maxMin = 0.0
# current best

for k,v in enumerate(minCap):
    #iterate all the items in minCap (each day) and divide by the day to get an average rate
    t = v/(k+1.0)
    # cumsum divided by the number of days since game start
    if t > maxMin:
        # if 't' is bigger than minMax, set minMax to t
        maxMin = t

maxMin
# this number will represent how much level capacity was needed to meet demand over the last two years

from math import ceil
# need the ceil function to calculate the setup costs of various shipments sizes
sCosts = lambda x: math.ceil(maxMin*730/(x*200))*1500
# and we are using a lambda function again

from numpy import arange
# import the arange function from Numpy to create a list of order quanitities

setups = DataFrame([sCosts(i) for i in range(1,10)], arange(200,2000,200))
# create a new data set using a list comprehension, and the arange function

setups.plot(ylim=[0,900000])
# we can see from this graph the pattern of diminishing returns in larger order quantities

# good enough for a quick look at the capability of pandas and Python to analyze data


