import pandas as pd
df = pd.DataFrame({
    'first_name': ['Sarah', 'John', 'Kyle', 'Joe'],
    'last_name': ['Connor', 'Connor', 'Reese', 'Bonnot'],
})
df.set_index('last_name', inplace=True)

result = df.loc[~df.index.duplicated(), :]
print(result)
