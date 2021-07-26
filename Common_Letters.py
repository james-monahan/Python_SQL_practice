# Find the top 3 most common letters across all the words from both the tables. 
# Output the letter along with the number of occurrences and order records in descending order based on the number of occurrences.

# Import your libraries
import pandas as pd

df2 = google_word_lists
df2['contents'] = df2.words1 + df2.words2
pd.concat([google_file_store, df2], axis=0)

df = pd.concat([google_file_store, df2], axis=0)
df['words'] = df.contents.str.split()
df = df['words'].explode().str.lower().to_frame()
df['letters'] = df['words'].apply(lambda x: [val for val in x])
df = df['letters'].explode().str.lower().to_frame()
df = df.groupby('letters').size().reset_index()
df.columns = ['letter', 'count']
df.sort_values(by='count', ascending=False).head(3)
