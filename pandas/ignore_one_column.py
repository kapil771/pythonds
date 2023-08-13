import pandas as pd
df = pd.DataFrame({
    'first_name': ['Sarah', 'John', 'Kyle', 'Joe'],
    'last_name': ['Connor', 'Connor', 'Reese', 'Bonnot'],
})

result = df.loc[:, df.columns != 'last_name']
print(result)
