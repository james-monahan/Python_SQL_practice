# Find the latest inspection date for the most sanitary restaurants. Assume the highest number of points is the most sanitary. 
# Only businesses with 'restaurants' in the name should be considered in your analysis.
# Output the corresponding facility name, inspection score, latest inspection date, previous inspection date, 
# and the difference between the latest and previous inspection dates. And order the records based on the latest inspection date in ascending order.

# Import your libraries
import pandas as pd

# Start writing code
df = los_angeles_restaurant_health_inspections
df = df[df.facility_name.str.contains('RESTAURANT')]
df = df[df['score']==df['score'].max()]
df = df[['facility_name', 'score', 'activity_date']]
df['rank'] = df.groupby('facility_name')['activity_date'].rank(ascending=False)
df1 = df[df['rank']==1]
df1 = df1.merge(df[df['rank']==2], on='facility_name', how='left')
df1 = df1[['facility_name','score_x','activity_date_x','activity_date_y']]
df1['day_difference'] = (df1['activity_date_x']-df1['activity_date_y']).dt.days
df1.sort_values('activity_date_x')
