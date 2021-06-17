# Find the number of words in each business name. 
# Avoid counting special symbols as words (e.g. &). 
# Output the business name and its count of words.

# Import your libraries
import pandas as pd

# Start writing code
df = sf_restaurant_health_violations.drop_duplicates(subset='business_name')
df['no_punc'] = df.business_name.str.replace('[^A-Za-z0-9 ]', '', regex=True)
df = df[['business_name','no_punc']] 
df['no_punc'] = df['no_punc'].str.split().apply(len)
df
