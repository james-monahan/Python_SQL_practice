# Find the customer with the highest total order cost between 2019-02-01 to 2019-05-01. 
# Output their first name, total cost of their items, and the date.
# For simplicity, you can assume that every first name in the dataset is unique.

# Import your libraries
import pandas as pd

mask = orders['order_date'].between("2019-02-01","2019-05-01")
orders = orders[mask]

orders['total'] = orders['order_quantity']*orders['order_cost']
orders['order_date'] = orders['order_date'].dt.date

name = zip(customers['id'], customers['first_name'])
mapping = {k:v for k,v in name}
orders['cust_id'] = orders['cust_id'].map(mapping)

orders = orders.groupby(['cust_id', 'order_date'], as_index=False)\
['total'].sum()

orders.nlargest(1, 'total', keep='all')
