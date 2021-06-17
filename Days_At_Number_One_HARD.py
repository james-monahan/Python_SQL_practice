# You have a table with US rankings of tracks and another table with worldwide rankings of tracks.

# Find the number of days a US track has stayed in the 1st position for both the US and worldwide 
# rankings. Output the track name and the number of days in the 1st position. Order your output 
# alphabetically by track name.

# Import your libraries
import pandas as pd

# Start writing code
df_us = spotify_daily_rankings_2017_us
df_intl = spotify_worldwide_daily_song_ranking
df_intl=df_intl[df_intl.position==1]

df = df_us.merge(df_intl, on=['trackname', 'date'])
df.groupby('trackname')['position_x'].count().reset_index().sort_values(by='trackname')

