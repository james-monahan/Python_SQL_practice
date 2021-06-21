# Given a table of purchases by date, calculate the month-over-month percentage change in revenue. 
# The output should include the year-month date (YYYY-MM) and percentage change, rounded to the 2nd 
# decimal point, and sorted from the beginning of the year to the end of the year.
# The percentage change column will be populated from the 2nd month forward and can be calculated as 
# ((this month's revenue - last month's revenue) / last month's revenue)*100.

# Import your libraries
import pandas as pd

# Start writing code
df = sf_transactions
df['month_year'] = df.created_at.dt.to_period('M')
df = df.groupby('month_year', as_index=False)['value'].sum()
df['prior_mo'] = df.value.shift(1)
df['pct_change'] = (((df['value']-df['prior_mo'])/df['prior_mo'])*100).round(2)
df[['month_year', 'pct_change']]

# (sf_transactions.groupby(sf_transactions.created_at.dt.to_period("M")).value.sum().pct_change()*100).reset_index().round(2)
