# Find all people who earned more than the average in 2013 for their designation 
# but were not amongst the top 5 earners for their job title. Use the totalpay 
# column to calculate total earned and output the employee name(s) as the result.

# Import your libraries
import pandas as pd

# Start writing code
df = sf_public_salaries[sf_public_salaries['year']==2013]
df['rank'] = df.groupby('jobtitle')['totalpay'].rank(method='dense', ascending=False)
df['avg_salary_dept'] = df.groupby('jobtitle')['totalpay'].transform('mean')
df = df[(df['totalpay']>df['avg_salary_dept']) &\
        (df['rank']>5)][['employeename']]
