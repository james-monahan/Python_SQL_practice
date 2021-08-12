# Find the average host response rate with a cleaning fee for each zipcode. Present the results as a percentage along with the zip code value. 
# Convert the following two columns while building the query to their true types using type casts and if necessary string processing: 
# 'cleaning_fee' from TEXT to BOOL and 'host_response_rate' from TEXT to NUMERIC (take missing values as NULL). 
# Order the result in ascending order based on the average host response rater after cleaning. 

# Import your libraries
import pandas as pd

# Start writing code
df = airbnb_search_details
df = df[df['cleaning_fee']==True]
df['host_response_rate'] = df['host_response_rate'].str.replace('%', '')
df['host_response_rate'] = pd.to_numeric(df['host_response_rate'])
df = df[['host_response_rate', 'zipcode']]
df.groupby('zipcode')['host_response_rate'].mean()\
            .reset_index().sort_values('host_response_rate').dropna()

