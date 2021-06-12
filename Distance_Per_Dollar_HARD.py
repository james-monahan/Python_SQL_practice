# You’re given a dataset of uber rides with the traveling distance (‘distance_to_travel’) and cost (‘monetary_cost’) for each ride. 
# For each date, find the difference between the distance-per-dollar for that date and the average distance-per-dollar for that year-month. 
# Distance-per-dollar is defined as the distance traveled divided by the cost of the ride.
# The output should include the year-month (YYYY-MM) and the average difference in distance-per-dollar 
# for said year-month as an absolute value rounded to the 2nd decimal. You should also count both success and 
# failed request_status as the distance and cost values are populated for all ride requests. Also, assume that 
# all dates are unique in the dataset. Order your results by earliest request date first.

# Import your libraries
import pandas as pd

uber_request_logs['month_year'] = uber_request_logs.request_date.dt.strftime('%Y-%m')
uber_request_logs['distance_per_dollar'] = uber_request_logs['distance_to_travel']  / uber_request_logs['monetary_cost']

avg_amts = uber_request_logs.groupby('month_year')['distance_per_dollar'].mean().reset_index()
avg_amts.columns = ['month_year', 'avg_distance_per_dollar']

uber_request_logs = uber_request_logs.merge(avg_amts, on='month_year')

uber_request_logs['difference_between'] = abs(uber_request_logs['distance_per_dollar'] - uber_request_logs['avg_distance_per_dollar']).round(2)

uber_request_logs.groupby('month_year')['difference_between'].mean().reset_index()
