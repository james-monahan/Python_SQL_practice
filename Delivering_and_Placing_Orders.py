# Check if there is a correlation between Total Order value and time in minutes 
# between placing the order and delivering the order per restaurant.

# Import your libraries
import pandas as pd

# Start writing code
df = doordash_delivery
df['time_to_dest_min'] = ((df.delivered_to_consumer_datetime - df.customer_placed_order_datetime)/60)
df = df[['time_to_dest_min', 'order_total', 'restaurant_id']]
df['time_to_dest_min'] = df['time_to_dest_min'].astype('int')/1000000000
df.groupby('restaurant_id').mean().corr().values[0,1]

#dt.total_seconds() returns float
