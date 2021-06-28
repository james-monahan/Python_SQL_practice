# Find the percentage of shipable orders.
# Consider an order is shipable if the customer's address is known.

# Import your libraries
import pandas as pd

# Start writing code
order_len = len(orders)
customers = customers[~customers.address.isna()]
order_len_shipable = len(orders.merge(customers, left_on='cust_id', right_on='id'))
(order_len_shipable/order_len)*100
