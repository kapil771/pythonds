import pandas as pd

result = pd.Timestamp('9/27/22').tz_localize('US/Pacific')
print(result)
