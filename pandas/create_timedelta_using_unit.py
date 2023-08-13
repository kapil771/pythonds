import pandas as pd

result = pd.to_timedelta(1, unit='h')
print(result)


result = pd.Timedelta(days=2)
print(result)

result = pd.Timedelta(minutes=2)
print(result)

result = pd.Timedelta(seconds=2)
print(result)
