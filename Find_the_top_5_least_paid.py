# Find the top 5 least paid employees for each job title. 
# Output the job title along with the corresponding first 
# 5 least paid employees with their total pay with benefits.

# Import your libraries
import pandas as pd

# Start writing code
sf_public_salaries['rank'] = sf_public_salaries\
    .groupby('jobtitle')['totalpaybenefits'].rank('first')
    
df = sf_public_salaries[['jobtitle','employeename','rank','totalpaybenefits']]
df[df['rank']<=5].sort_values(['jobtitle', 'employeename'])

