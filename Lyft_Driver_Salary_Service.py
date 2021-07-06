# Find the correlation between the annual salary and the length of the service period of a Lyft driver.

import pandas as pd

# Start writing code
lyft_drivers.end_date.fillna(pd.Timestamp.now(), inplace=True)
lyft_drivers['service'] = (lyft_drivers.end_date - lyft_drivers.start_date)\
                          .dt.days
lyft_drivers[['service', 'yearly_salary']].corr().values[0,1]
