import pandas as pd
df = pd.DataFrame({
    'request': ['GET /index.html?baz=3', 'GET /foo.html?bar=1'],
})

filtered_data = df['request'].str.extract('GET /([^?]+)\?', expand=True)
print('filtered_data::::', filtered_data)
