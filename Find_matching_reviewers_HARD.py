# Find matching reviewers in a way that each host is paired with a matching guest based on the given review scores.
# ex: pair a guest reviewer who gave 1 with a host reviewer who gave the same score.
# Output host id, guest id, and the corresponding review score. Present distinct review scores only.
# Order recording by review score in descending order.

# Import your libraries
import pandas as pd

# Start writing code
hosts = airbnb_reviews[airbnb_reviews['from_type']=='host']
guests = airbnb_reviews[airbnb_reviews['from_type']=='guest']
df = hosts.merge(guests, on='review_score')
df.drop_duplicates(subset=['review_score']).sort_values(by='review_score',ascending=False)[['from_user_x', 'from_user_y', 'review_score']]
