import pandas as pd

last_names = ['Connor', 'Connor', 'Reese']
first_names = ['Sarah', 'John', 'Kyle']
df = pd.DataFrame({
    'first_name': first_names,
    'last_name': last_names,
})
print(df)
