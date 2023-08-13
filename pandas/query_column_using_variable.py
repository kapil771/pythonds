import pandas as pd
df = pd.DataFrame(data={
    'first_name': ['Sarah', 'John', 'Kyle'],
    'last_name': ['Connor', 'Connor', 'Reese'],
})

column_name = 'first_name'
search = df.query(f"`{column_name}` == 'John'")
print(search)
