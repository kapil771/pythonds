import pandas as pd
df = pd.DataFrame({
    'first_name': ['Sarah', 'John', 'Kyle'],
    'last_name': ['Connor', 'Connor', 'Reese'],
})

result = df[df['last_name'].map(len) == 5]
print(result)
