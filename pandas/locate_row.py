import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45],
    "test": [10, 20, 30]
}

# load data into a DataFrame object:
df = pd.DataFrame(data)
print(df.loc[0])
print('====================================')
print(df.loc[1])
print('====================================')
print(df.loc[2])
print('====================================')
if 3 in df:
    print(df.loc[3])

print('====================================')
# use a list of indexes:
print(df.loc[[0, 1]])
# Note: When using [], the result is a Pandas DataFrame.
