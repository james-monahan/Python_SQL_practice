# Find the 3-month rolling average of total revenue from purchases given a table with users, their purchase amount, 
# and date purchased. Do not include returns which are represented by negative purchase values. Output the month and 
# 3-month rolling average of revenue, sorted from earliest month to latest month.
# A 3-month rolling average is defined by calculating the average total revenue from all user purchases for the current 
# month and previous two months. The first two months will not be a true 3-month rolling average since we are not given data from last year.

# Import your libraries
import pandas as pd

# Start writing code
amazon_purchases = amazon_purchases[amazon_purchases['purchase_amt'] > 0]
amazon_purchases['created_at'] = amazon_purchases['created_at'].dt.strftime('%Y-%m')
mo_purchases = amazon_purchases.groupby('created_at', as_index=False)['purchase_amt'].sum().sort_values('created_at')
mo_purchases['mo_rev'] = mo_purchases.purchase_amt.rolling(window=3, min_periods=1).mean()
mo_purchases[['created_at','mo_rev']]

# df['date'] = pd.to_datetime(df['created_at']).dt.to_period("M")
# res["prev_1"] = res["purchase_amt"].shift(1)
# res["prev_2"] = res["purchase_amt"].shift(2)
