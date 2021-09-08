# Find the list of intersections between both word lists.

# Import your libraries
import pandas as pd

# Start writing code
df = google_word_lists
word1 = set(df['words1'].str.split(',', expand=True).stack())
word2 = set(df['words2'].str.split(',', expand=True).stack())
list(word1.intersection(word2))
