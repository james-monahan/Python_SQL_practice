# Find the number of police officers, firefighters, and medical staff employees based on the employee name.
# Output each job title along with the corresponding number of employees.

# Import your libraries
import pandas as pd

# Start writing code

# sf_public_salaries.jobtitle.unique()
job_titles = ['firefighter', 'police', 'medical']
df = sf_public_salaries
df['jobtitle2'] = df['jobtitle'].str.replace(r'[/|(|)]', ' ').str.lower()
df['jobtitle2'] = df['jobtitle2'].str.split()
df['jobtitle2'] = df['jobtitle2'].apply\
        (lambda x: [val for val in x if val in job_titles])
df['jobtitle2'] = df['jobtitle2'].apply(lambda x: x[0] if len(x)>0 else None)
df.groupby('jobtitle2').size().reset_index()


