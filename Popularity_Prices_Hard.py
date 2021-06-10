#You’re given a table of rental property searches by users. 
#The table consists of search results and outputs host information for searchers. 
#Find the minimum, average, maximum rental prices for each host’s popularity rating. 
#The host’s popularity rating is defined as below:
#    0 reviews: New
#    1 to 5 reviews: Rising
#    6 to 15 reviews: Trending Up
#    16 to 40 reviews: Popular
#    more than 40 reviews: Hot

# Import your libraries
import pandas as pd

unique_id = ['price', 'room_type', 'host_since', 'zipcode', 'number_of_reviews']
airbnb_host_searches.drop_duplicates(subset=unique_id, inplace=True)

def change_val(x):
    if x == 0: 
        return 'New'
    elif x in range(1,6):
        return 'Rising'
    elif x in range(6,16):
        return 'Trending Up'
    elif x in range(16,41):
        return 'Popular'
    else:
        return 'Hot'

airbnb_host_searches['number_of_reviews'] = airbnb_host_searches['number_of_reviews'].apply(change_val)

airbnb_host_searches.groupby(['number_of_reviews'])\
      .price.agg(['min','mean', 'max']).reset_index()
