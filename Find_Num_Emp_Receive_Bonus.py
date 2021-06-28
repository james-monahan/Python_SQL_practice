# Find the number of employees who received the bonus and who didn't.
# Output an indication of whether the bonus was received or not along 
# with the corresponding number of employees.
# ex: if the bonus was received: 1, if not: 0.

# Import your libraries
import pandas as pd

# Start writing code
df = employee.merge(bonus, how='outer', left_on='id', right_on='worker_ref_id')
df['bonus_amount'] = df['bonus_amount'].apply(lambda x: x/x).fillna(0)
df.groupby('bonus_amount').size()
