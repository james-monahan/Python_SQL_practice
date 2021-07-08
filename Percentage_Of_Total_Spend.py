# Find the percentage of the total spend a customer spent on each order. 
# Output the customer’s first name, order details, and percentage of their 
# total spend for each order transaction rounded to the nearest whole number. 
# Assume each customer has a unique first name (i.e., there is only 1 customer 
# named Karen in the dataset).



# Import your libraries
import pandas as pd

# Start writing code
df = orders.merge(customers, left_on='cust_id', right_on='id')
df = df[['first_name', 'order_details', 'order_cost']]
df['total_order'] = df.groupby('first_name', as_index=False)\
                    ['order_cost'].transform('sum')
df['percent_total'] = round((df['order_cost']/df['total_order'])*100)
df.groupby(['first_name', 'order_details'], as_index=False)['percent_total'].sum()
