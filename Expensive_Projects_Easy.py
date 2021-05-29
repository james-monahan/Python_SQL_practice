# Given a list of projects and employees mapped to each project, calculate by the amount of project budget allocated to each employee . 
# The output should include the project title and the project budget per employee as an integer. 
# Order your list by projects with the highest budget per employee first.

import pandas as pd

# Start writing code
db = pd.merge(ms_projects, ms_emp_projects, left_on='id', right_on='project_id')
df_bud = db.groupby('title', as_index=False).agg({'budget':['max'], 'emp_id':['count']}).sort_values(('budget', 'max'), ascending=False)
df_bud[('budget', 'ratio')] = df_bud[('budget', 'max')] // df_bud[('emp_id', 'count')]
df_bud[[('title', ''),('budget', 'ratio')]]
