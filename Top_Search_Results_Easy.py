# You're given a table that contains search results. 
# If the 'position' column represents the position of the search results, 
# write a query to calculate the percentage of search results that were in the top 3 position.

# Import your libraries
import pandas as pd
sum(fb_search_results['position'].value_counts(normalize=True, sort=False)[:3])*100
