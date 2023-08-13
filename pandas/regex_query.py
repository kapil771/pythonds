import pandas as pd
df = pd.DataFrame({
    'first_name': ['Sarah', 'John', 'Kyle', 'Joe'],
    'last_name': ['Connor', 'Connor', 'Reese', 'Bonnot'],
})

search = df[df.last_name.str.match('.*onno.*')]
first_name_search = df[df.first_name.str.match('.*le.*')]

# print(df.last_name)
print(search)
print('===================================================')
print(first_name_search)
