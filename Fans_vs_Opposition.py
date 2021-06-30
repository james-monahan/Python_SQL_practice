# Facebook is quite keen on pushing their new programming language Hack to all 
# their offices. They ran a survey to quantify the popularity of the language 
# and send it to their employees. To promote Hack they have decided to pair 
# developers which love Hack with the ones who hate it so the fans can convert 
# the opposition. Their pair criteria is to match the biggest fan with biggest 
# opposition, second biggest fan with second biggest opposition, and so on. Write 
# a query which returns this pairing. Output employee ids of paired employees 
# and sort users with the same popularity value by id in ascending order. 
# You can limit the number of rows to 7 so that the employees don't repeat.

# Import your libraries
import pandas as pd

# Start writing code
df1 = facebook_hack_survey.sort_values(by='popularity').reset_index(drop=True)
df2 = facebook_hack_survey.sort_values(by='popularity', ascending=False).reset_index(drop=True)
df3 = pd.concat([df2,df1], axis=1)
df3[['employee_id']].head(7)
