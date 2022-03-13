from datetime import timedelta

import pandas as pd


# Specify start and periods, the number of periods (days).
# dRan1 = pd.date_range(start='2017-01-01', periods=13, inclusive='right')

def test_something(a, b):
    return {b, a}


print(test_something(1, 1))

exit(1)

for d in pd.date_range(start='2022-02-01', periods=10, inclusive='left'):
    original_date = pd.to_datetime(d).date()
    next_date = pd.to_datetime(d).date() + timedelta(days=1)
    strptime = next_date.strftime("%Y-%m-%d")
    print('Original {}-{}, New {}-{}'.format(original_date, type(original_date), strptime, type(strptime)))

new_date = pd.to_datetime('2022-02-01').date()
print(new_date, type(new_date))
updated_date = (new_date + timedelta(days=10)).strftime("%Y-%m-%d")
print(updated_date, type(updated_date))


def calculation(x, y):
    return lambda a, b: {x + y, x - y}


f = calculation(4, 2)
print(f(4, 2))
