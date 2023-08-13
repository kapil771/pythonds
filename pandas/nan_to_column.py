import numpy as np
import pandas as pd
df = pd.DataFrame({
    'dogs': [5, 10, np.nan, 7],
})

result = df['dogs'].replace(np.nan, 0, regex=True)
print(result)
