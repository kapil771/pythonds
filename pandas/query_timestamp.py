import pandas as pd

peoples = {
    'first_name': ['kapil', 'akash', 'moksh'],
    'last_name': ['kumar', 'varshney', 'sharma'],
    'age': [30, 25, 2],
    'time': ['2022/09/14 00:52:00-07:00', '2022/09/14 00:52:30-07:00',
             '2022/09/14 01:52:30-07:00']
}
df = pd.DataFrame(peoples, index=[1, 2, 3])
df['time'] = pd.to_datetime(df.time)
search = df.query('time >= "2022-09-14 00:52:00-07:00"')
print(search)
