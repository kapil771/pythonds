import pandas as pd
df = pd.DataFrame({
    'date': ['9/1/22', '9/2/22', '9/3/22'],
    'action': ['Add', 'Update', 'Delete'],
    'msg_ids': [[1, 2, 3], [1, 2], [2, 3]],
})
df.set_index('date', inplace=True)


temp_series = df['msg_ids'].apply(pd.Series, 2).stack()
temp_series.index = temp_series.index.droplevel(-1)
temp_series.name = 'msg_id'
new_df = temp_series.to_frame()
new_df.set_index('msg_id', inplace=True)
result = new_df.loc[~new_df.index.duplicated(), :]  # Drop duplicates.
print('==============================================================')
print(result)
