import pandas as pd
df = pd.DataFrame({
    'time': ['2022-09-14 00:52:00-07:00', '2022-09-14 00:52:30-07:00',
             '2022-09-14 01:52:30-07:00'],
    'letter': ['A', 'B', 'C'],
})
print(df)
print('==================================================')
df['time'] = pd.to_datetime(df.time)
# describe treat datetime stamp like objects that's why need "datetime_is_numeric=True"
df['time'].describe(datetime_is_numeric=True)
print(df)
