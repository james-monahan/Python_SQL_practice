# Select the most popular client_id based on a count of the number of users who have at least 50% 
# of their events from the following list: 'video call received', 'video call sent', 'voice call received', 'voice call sent'.

# Import your libraries
import pandas as pd

# Start writing code
event_list = ['video call received', 'video call sent', 
'voice call received', 'voice call sent']

fact_events['event_counts'] = fact_events['event_type'].apply(lambda x: 1 if x in event_list else 0)
filter_ = fact_events.groupby('user_id')['event_counts'].agg({'sum_':'sum','count_':'count'})
users = filter_[filter_['sum_']/filter_['count_'] >= .5].index
fact_events = fact_events[fact_events['user_id'].apply(lambda x: x in users)]
fact_events.groupby('client_id').count().reset_index()['client_id'][0]

# .isin([vals])
