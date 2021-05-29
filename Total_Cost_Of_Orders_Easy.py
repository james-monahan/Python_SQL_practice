# Find the total cost of each customer's orders. Output customer's id, 
# first name, and the total order cost. Order records by customer's 
# first name alphabetically.

# Import your libraries
import pandas as pd

customers = customers[['id', 'first_name']]
orders = orders[['cust_id', 'order_cost']]

m = pd.merge(customers, orders, \
             left_on='id', right_on='cust_id')
             
m.groupby(['id', 'first_name'], as_index=False)['order_cost']\
         .sum().sort_values('first_name')
