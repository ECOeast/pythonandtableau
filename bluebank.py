# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 14:41:28 2022

@author: Erik
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Method 1 to read json data
json_file = open('loan_data_json.json')
data = json.load(json_file)

# Method 2 to read  json data
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
    
# Transform to dataframe
loandata = pd.DataFrame(data)

# Find unique values in column
loandata['purpose'].unique()

# Describe the data
loandata.describe()

# Describe column
loandata['int.rate'].describe()

# Using exp() to get annual income
loandata['annualincome'] = np.exp(loandata['log.annual.inc'])

# fico >= 300 and < 400:'Very Poor'
# fico >= 400 and ficoscore < 600:'Poor'
# fico >= 601 and ficoscore < 660:'Fair'
# fico >= 660 and ficoscore < 780:'Good'
# fico >=780:'Excellent'

ficocat = []
for fico in loandata['fico']:
    try:
        if fico >= 300 and fico < 400: cat = 'Very Poor'
        elif fico >= 400 and fico < 600: cat = 'Poor'
        elif fico >= 600 and fico < 660: cat = 'Fair'
        elif fico >= 660 and fico < 780: cat = 'Good'
        elif fico >= 780: cat = 'Excellent'
        else: cat = 'Unknown'
    except:
        cat = 'Unknown'
    ficocat.append(cat)
    
loandata['ficocat'] = ficocat

# df.loc as conditional statements
# df.loc[df[columnname] condition, newcolumnname] = 'value if condition is met'
loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

# plot ficocat
catplot = loandata.groupby(['ficocat']).size()
catplot.plot.bar(color = 'pink')
plt.show()

# plot purpose
purposeplot = loandata.groupby(['purpose']).size()
purposeplot.plot.bar()
plt.show

# scatter plot
xpoint = loandata['annualincome']
ypoint = loandata['dti']
plt.scatter(xpoint, ypoint)
plt.show()

# writing to CSV file
loandata.to_csv('loan_cleaned.csv', index=True)






