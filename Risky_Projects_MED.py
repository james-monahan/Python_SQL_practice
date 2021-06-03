#Identify projects that are at risk for going overbudget. A project is considered to be 
#overbudget if the cost of all employees assigned to the project is greater than the budget of the project. 
#You'll need to prorate the cost of the employees to the duration of the project. For example, 
#if the budget for a project that takes half a year to complete is $10K, then the total half-year salary 
#of all employees assigned to the project should not exceed $10K. Output a list of projects that are 
#overbudget with their project name, project budget, and prorated total employee expense (rounded to the next dollar amount).

# Import your libraries
import pandas as pd

# Start writing code
linkedin_projects['date_diff'] = (linkedin_projects.end_date\
                                  -linkedin_projects.start_date).dt.days
                                  

df = linkedin_projects.merge(linkedin_emp_projects,\
                             left_on='id', right_on="project_id")
       
df = df.merge(linkedin_employees,left_on='emp_id', right_on="id")
         
df = df.groupby(['title', 'budget','date_diff'], as_index=False)['salary'].sum()

df['expense'] = round((df['salary'] * df['date_diff'])/365)

df.loc[df.expense>df.budget, ['title', 'budget', 'expense']]

