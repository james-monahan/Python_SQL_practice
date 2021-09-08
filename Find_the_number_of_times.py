# Find the number of times each word appears in drafts.
# Output the word along with the corresponding number of occurrences.

import pandas as pd

df = google_file_store[google_file_store.filename.str.contains('draft')]
df['contents'].str.split(expand=True).stack().value_counts()
