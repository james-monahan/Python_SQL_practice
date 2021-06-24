# Find the genre of the person with the most number of oscar winnings.
# If there are more than one person with the same number of oscar wins, 
# return the first one in alphabetic order.

# Import your libraries
import pandas as pd

# Start writing code
wins = oscar_nominees.groupby('nominee', as_index=False)['winner'].sum().sort_values(by='winner', ascending=False)

winner = wins[wins.winner == wins.winner.max()].sort_values('nominee').head(1)
winner = winner['nominee'].values[0]

nominee_information[nominee_information['name'] == winner]['top_genre']
