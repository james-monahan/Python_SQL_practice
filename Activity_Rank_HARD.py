# Find the email activity rank for each user. Email activity rank is defined by the 
# total number of emails sent. The user with the highest number of emails sent will 
# have a rank of 1, and so on. Output the user, total emails, and their activity rank. 
# Order records by the total emails in descending order. Sort users with the same rank 
# score in alphabetical order. In your rankings, return a unique value (i.e., a unique percentile) 
# even if multiple users have the same number of emails.

# Import your libraries
import pandas as pd

# Start writing code
emails = google_gmail_emails.groupby('from_user', as_index=False).count()
emails = emails.sort_values(by=['id', 'from_user'], ascending=[False, True]).reset_index()
emails['rank'] = emails.index + 1 
emails = emails[['from_user', 'id', 'rank']]  
emails.columns = ['from_user', 'count', 'rank']
emails

# result['rank']=result['total_emails'].rank(method='first',ascending=False)
