# Write a query that returns a list of the bottom 2% revenue generating restaurants. 
# Return a list of restaurant IDs and their total revenue from when customers placed orders in May 2020.

# You can calculate the total revenue by summing the order_total column. 
# And you should calculate the bottom 2% by partitioning the total revenue into evenly distributed buckets.

# Import your libraries
import pandas as pd

# Start writing code
df = doordash_delivery
month = (df.customer_placed_order_datetime.dt.month == 5)
year = (df.customer_placed_order_datetime.dt.year == 2020)
df = df[month & year][['restaurant_id', 'order_total']]
df = df.groupby('restaurant_id', as_index=False)['order_total'].sum()
df[df['order_total'] <= df['order_total'].quantile(.02)][['restaurant_id', 'order_total']].sort_values(by='order_total', ascending=False)
