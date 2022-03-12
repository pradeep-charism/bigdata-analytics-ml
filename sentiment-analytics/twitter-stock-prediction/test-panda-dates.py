import pandas as pd
from datetime import timedelta, datetime

# Specify start and periods, the number of periods (days).
# dRan1 = pd.date_range(start='2017-01-01', periods=13, inclusive='right')

for d in pd.date_range(start='2022-02-01', periods=5):
    date = pd.to_datetime(d).date() + timedelta(days=1)
    strptime = date.strftime("%Y-%m-%d")
    print(strptime)
    print(type(strptime))
