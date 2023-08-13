import pandas as pd
df = pd.DataFrame({
    'time': ['2022/09/14 00:52:00-07:00', '2022/09/14 00:52:30-07:00',
             '2022/09/14 01:52:30-07:00'],
    'letter': ['A', 'B', 'C'],
})
df['time'] = pd.to_datetime(df.time)

begin_ts = '2022/09/14 00:52:30-07:00'
end_ts = '2022/09/14 01:53:30-07:00'
search = df.query('@begin_ts<=time<@end_ts')
print(search)
