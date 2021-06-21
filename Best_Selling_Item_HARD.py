# Find the best selling item for each month where the biggest total invoice was paid. 
# The best selling item is calculated using the formula (unitprice * quantity). 
# Output the description of the item along with the amount paid.

# Import your libraries
import pandas as pd

# Start writing code
online_retail['month'] = online_retail['invoicedate'].dt.month
online_retail['total_invoice'] = online_retail['quantity'] * online_retail['unitprice']
or_max = online_retail[['month', 'total_invoice', 'description']]
or_max = or_max.groupby(['month','description'], as_index=False)['total_invoice'].sum()
or_mo_max = or_max.groupby('month', as_index=False)['total_invoice'].max()
or_max.merge(or_mo_max, on=['month','total_invoice'])

# df['rank'] = df.groupby('month')['total_amount'].rank(method='max',ascending=False)
# final=df[df['rank']==1][['month', 'description','total_amount']]
