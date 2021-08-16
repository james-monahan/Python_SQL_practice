Sort the words alphabetically in 'final.txt' and make a new file named 'wacky.txt'. 
Output the file contents in one column and the filename 'wacky.txt' in another column.

# Import your libraries
import pandas as pd

# Start writing code
df = google_file_store
df_text = df[df['filename']=='final.txt']['contents']

text = df_text.to_list()[0].split()
sorted_list = sorted(text, key=lambda x: x.lower())
d = {'filename': 'wacky.txt', 'contents': [sorted_list]}
pd.DataFrame(data=d)
