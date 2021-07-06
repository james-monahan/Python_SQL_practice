# Find whether the number of drivers that have churned increased or decreased 
# in each year compared to the previous one. Output the year (specifically, 
# you can use the year the driver left Lyft) along with the corresponding 
# number of churns in that year, the number of churns in the previous year, 
# and an indication on whether the number has been increased (output the value 
# 'increase') or decreased (output the value 'decrease'). Order records by the year in ascending order.

# Import your libraries
import pandas as pd

# Start writing code
lyft_drivers['year'] = lyft_drivers.end_date.dt.year
lyft_drivers['end_date'] = lyft_drivers.end_date.notnull().astype('int')
lyft_drivers = lyft_drivers.groupby('year', as_index=False)['end_date'].sum()
lyft_drivers.columns = ['year', 'amt_churn']
lyft_drivers['prior_year'] = lyft_drivers.amt_churn.shift(1).fillna(0)
lyft_drivers['churn'] = (lyft_drivers.prior_year<lyft_drivers.amt_churn)\
            .astype('int').map({1: 'increase', 0: 'decrease'})
lyft_drivers
