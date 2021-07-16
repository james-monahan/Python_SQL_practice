# Write a query that returns every employee that has ever worked for the company. 
# For each employee, calculate the greatest number of employees that worked for 
# the company during their tenure and the first date that number was reached.

# Your output should have the employee ID, greatest number of employees that 
# worked for the company during the employee's tenure, and first date that number was reached.

# Import your libraries
import pandas as pd

df = uber_employees
df['hire_count'] = 1
df['term_count'] = df['termination_date']\
                .apply(lambda x: -1 if x < pd.Timestamp.now() else None)
df_hires = df[['hire_date', 'hire_count']]\
        .rename(columns={"hire_date": "date", "hire_count": "count"})
df_fires = df[['termination_date', 'term_count']]\
        .rename(columns={"termination_date": "date", "term_count": "count"})
df_counts = pd.concat([df_hires, df_fires]).dropna()
df_counts = df_counts.groupby('date', as_index=False)['count'].sum()
df_counts['cum_sum'] = df_counts['count'].cumsum()
df_counts

df['termination_date'].fillna(pd.Timestamp.now(), inplace=True)

def get_dates(data):
    temp = df_counts[(df_counts['date'] >= data['hire_date']) &\
        (df_counts['date'] <= data['termination_date'])]
    return temp[temp['cum_sum'] == temp['cum_sum'].max()]['date'].iloc[0:1].values[0]
def get_emp(data):
    temp = df_counts[(df_counts['date'] >= data['hire_date']) &\
        (df_counts['date'] <= data['termination_date'])]
    return temp[temp['cum_sum'] == temp['cum_sum'].max()]['cum_sum'].iloc[0:1].values[0]
    
df['min_date'] = df.apply(get_dates, axis=1)
df['max_emp'] = df.apply(get_emp, axis=1)
df[['id', 'max_emp', 'min_date']]
