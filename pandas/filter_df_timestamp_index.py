import pandas as pd
df = pd.DataFrame({
    'time': ['2022/09/14 00:52:00-07:00', '2022/09/14 00:52:30-07:00',
             '2022/09/14 01:52:30-07:00'],
    'letter': ['A', 'B', 'C'],
})
df['time'] = pd.to_datetime(df.time)
df.set_index('time', inplace=True)
filter_data = df.loc['2022-09-14':'2022-09-14 00:53']
# df.set_index('letter', inplace=True)
# filter_data = df.loc['A':'D']
print(df)
print(filter_data)
