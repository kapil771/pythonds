import pandas as pd
df = pd.DataFrame({
    'date': ['2022-09-14', '2022-09-15', '2022-09-16'],
    'letter': ['A', 'B', 'C'],
    'dict': [{'fruit': 'apple', 'weather': 'aces'},
             {'fruit': 'banana', 'weather': 'bad'},
             {'fruit': 'cantaloupe', 'weather': 'cloudy'}],
}, index=[1, 2, 3])
print(df.drop(['dict'], axis=1))
print('==============================================================')
print(df['dict'].apply(pd.Series))
print('==============================================================')
result = pd.concat(
    [df.drop(['dict'], axis=1), df['dict'].apply(pd.Series)], axis=1)
print(result)
