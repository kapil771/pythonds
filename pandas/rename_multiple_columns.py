import pandas as pd
df = pd.DataFrame({
    'Year': [2016, 2015, 2014, 2013, 2012],
    'Top Animal': ['Giant panda', 'Chicken', 'Pig', 'Turkey', 'Dog']
})

# df.rename(columns={
#     'Year': 'Calendar Year',
#     'Top Animal': 'Favorite Animal',
# }, inplace=False)

# df.columns = df.columns.str.replace("Year", "Calendar-Year")
# df.columns = df.columns.str.replace("Top Animal", "Favorite-Animal")
df.set_axis(["A", "B"], axis="columns", inplace=True)

print(df)
