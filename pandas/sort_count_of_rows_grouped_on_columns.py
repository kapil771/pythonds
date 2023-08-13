import pandas as pd
df = pd.DataFrame({
    'first_name': ['Sarah', 'John', 'Kyle'],
    'last_name': ['Connor', 'Connor', 'Reeses'],
})

result = df.groupby(['last_name']).size().sort_values(ascending=True)
print('================================================================')
print(result)
