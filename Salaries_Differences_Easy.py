# Write a query that calculates the difference between the highest salaries found in the marketing and engineering departments. 
# Output just the difference in salaries.

import pandas as pd

# Start writing code
db = pd.merge(db_employee, db_dept, left_on='department_id', right_on='id')
abs(max(db[db['department']=='marketing']['salary']) - \
max(db[db['department']=='engineering']['salary']))
