# Demonstration Code: Basic Marketing Efficiency Model
# Author:             Brad D. Messner 
# Date:               Feb 27, 2023 
# Description:        This tool will import a sample data file, categorize the data, and then perform a basic MEF Model.

# Import pandas and set our location to US for currency formatting
import pandas as pd
import locale
locale.setlocale( locale.LC_ALL, '' )

# Prompt the user for an acceptable ratio.  We will use this later to determine which sales channels performed at acceptable rates
desiredSEM = input('What is your desired Sales Efficieny Model Ratio? ')
desiredSEM = int(desiredSEM)

# Import our sales and sales data into panda dataframes
salesData = pd.read_csv ('/Users/bradmessner/Desktop/Pitt/salesData.csv')
salesExpense = pd.read_csv ('/Users/bradmessner/Desktop/Pitt/salesExpense.csv')

# Total all sales and output in local currency
totalSales = sum(salesData['Sales'])
locale.currency(totalSales, grouping=True)

# Total sale by category and output dataframe
salesData = salesData.groupby(['Channel'])['Sales'].sum()
salesData

# Total all sales related expenses and output in local currency
totalExpense = sum(salesExpense['Marketing Spend'])
locale.currency(totalExpense, grouping=True)

# Total sales expense by category and output dataframe
salesExpense = salesExpense.groupby(['Channel'])['Marketing Spend'].sum()
salesExpense

# Calculate the overall sales efficiency for our comapny and output result
overallSEF = totalSales / totalExpense
overallSEF

# Join our datafiles and calculate the sales efficiency for each channel; output the result
salesMerged = pd.merge(salesData, salesExpense, on='Channel')
salesMerged['SEM'] = salesMerged['Sales'] / salesMerged['Marketing Spend']
salesMerged

# Filter our dataframe down to only those greater than our desired sales efficiency ratio
preferredSEM = salesMerged[salesMerged['SEM'] > desiredSEM]
preferredSEM
