import pandas as pd
df = pd.DataFrame({
    'first_name': ['Sarah', 'John', 'Kyle'],
    'last_name': ['Connor', 'Connor', 'Reese'],
})

foo = 'Connor'
search = df.query('last_name == @foo')
print(search)
