# Write a query to find the number of days between the longest and least tenured 
# employee still working for the company. Your output should include the number 
# of employees with the longest-tenure, the number of employees with the least-tenure, 
# and the number of days between both the longest-tenured and least-tenured hiring dates.

# Import your libraries
import pandas as pd

# Start writing code
df = uber_employees[uber_employees.termination_date.isna()]
df['tenure'] = (pd.Timestamp.now() - df.hire_date).dt.days
df = df.groupby('tenure', as_index=False)['id'].count().iloc[[0,-1]]
days = df.iloc[1,0] - df.iloc[0,0]
min_tenure = df.iloc[0,1]
max_tenure = df.iloc[1,1]
pd.DataFrame({'shortest':[min_tenure],'max':[max_tenure],'diff':[days]})
