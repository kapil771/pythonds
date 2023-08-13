import pandas as pd

result = pd.Timestamp('9/27/22').tz_localize('US/Pacific')
print(result)

result = pd.Timestamp('9/27/22 06:59').tz_localize('US/Pacific')
print(result)
