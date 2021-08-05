#Find the top 3 medal-winning teams by counting the total number of medals 
#for each event in the Rio De Janeiro 2016 olympics. Output the event 
#name along with the top 3 teams as the 'gold team', 'silver team', and 
#'bronze team', with the team name and the total medals under each column.

# Import your libraries
import pandas as pd

# Start writing code
df = olympics_athletes_events
df = df[(df['year'] == 2016) & (df['city'] == 'Rio de Janeiro')]
df = df.groupby(['event', 'team'])['medal'].count().reset_index()
df = df[df['medal']>0]
df['text'] = df['team'] + ' with '+ df['medal'].astype('str') + ' medal/s'
df['rank'] = df.groupby('event')['medal'].rank(method='first', ascending=False)
gold = df[df['rank']==1][['event','text']]
silver = df[df['rank']==2][['event','text']]
bronze = df[df['rank']==3][['event','text']]
df = gold.merge(silver, how='outer', on='event').merge(bronze, how='outer', on='event')
df.columns = ['event', 'gold_team', 'silver_team', 'bronze_team']
df
