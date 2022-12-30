# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 13:42:10 2022

@author: Erik
"""

import pandas as pd

# file_name = pd.read_csv(file.csv) <--- format
data = pd.read_csv('transaction.csv', sep=';')

# summary of the data
data.info()

# variables = dataframe['column_name']

# Add new column to dataframe
data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']
data['Markup'] = data['ProfitPerTransaction'] / data['CostPerTransaction']

# Rounding function
data['Markup'] = round(data['Markup'], 2)

# Combining data fields
data['date'] = data['Day'].astype(str) + '-' + data['Month'] + '-' + data['Year'].astype(str)

# Splitting Column
# new_var = column.str.split('sep', expand = True)
split_col = data['ClientKeywords'].str.split(',', expand = True)
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

# Fixing new columns with replace function
data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']', '')

# Using lower function to change string to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

# Bringing in new dataframe
seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

# Merging files
# merge_df = pd.merge(df_old, df_new, on = 'key')
data = pd.merge(data, seasons, on = 'Month')

# Remove columns
# df = df.drop('ColumnName', axis = 1)
data = data.drop(['ClientKeywords','Year','Month','Day'], axis=1)

# Export to CSV file
data.to_csv('ValueInc_Cleaned.csv', index=False)







