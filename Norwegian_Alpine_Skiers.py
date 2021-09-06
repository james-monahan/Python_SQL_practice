# Find all Norwegian alpine skiers who participated in 1992 but didn't participate in 1994. Output unique athlete names.

# Import your libraries
import pandas as pd

# Start writing code
df = olympics_athletes_events
names_1992 = df[(df.noc=='NOR') & df.event.str.contains('Alpine') & df.year.isin([1992])]['name']
names_1994 = df[(df.noc=='NOR') & df.event.str.contains('Alpine') & df.year.isin([1994])]['name']
names = (set(names_1992).difference(set(names_1994)))
list(names)
