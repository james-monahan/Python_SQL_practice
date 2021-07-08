# Facebook's web logs capture every action from users starting from page 
# loading to page scrolling. Find the user with the least amount of time 
# between a page load and their first scroll down. Your output should include 
# the user id, page load time, first scroll down time, and time between the 
# two events in seconds.


# Import your libraries
import pandas as pd

# Start writing code
facebook_web_log['mo_date'] = facebook_web_log['timestamp']\
         .astype('str').apply(lambda x:x[5:10])
df_load = facebook_web_log[facebook_web_log.action == 'page_load']
df_action = facebook_web_log[facebook_web_log.action != 'page_load']

df_load = df_load.groupby(['user_id', 'mo_date'], as_index=False)\
         ['timestamp'].max()
df_action = df_action.groupby(['user_id', 'mo_date'], as_index=False)\
         ['timestamp'].min()
       
df = df_load.merge(df_action, on=['user_id', 'mo_date'])
df['time'] = df.timestamp_y - df.timestamp_x
df[df.time == df.time.min()].drop('mo_date', axis=1)
