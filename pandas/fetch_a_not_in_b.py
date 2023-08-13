import pandas as pd
terminator_df = pd.DataFrame({
    'first_name': ['Sarah', 'John', 'Kyle'],
    'last_name': ['Connor', 'Connor', 'Reese'],
})
terminator_df.set_index('first_name', inplace=True)

buckaroo_df = pd.DataFrame({
    'first_name': ['John', 'John', 'Buckaroo'],
    'last_name': ['Parker', 'Whorfin', 'Banzai'],
})
buckaroo_df.set_index('first_name', inplace=True)

result = terminator_df[~terminator_df.index.isin(buckaroo_df.index)]
print(result)
