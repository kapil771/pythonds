# import pandas
import pandas as pd

# create data frame
df = pd.DataFrame({'First Name': ["Mukul", "Rohan", "Mayank",
                                  "Vedansh", "Krishna"],

                   'Location': ["Saharanpur", "Rampur", "Agra",
                                "Saharanpur", "Noida"],

                   'Pay': [56000.0, 55000.0, 61000.0, 45000.0, 62000.0]})

# print original data frame
print(df)
print('=======================================================================')
# create a dictionary
# key = old name
# value = new name
dict = {'First Name': 'Name',
        'Location': 'City',
        'Pay': 'Salary'}

# call rename () method
df.rename(columns=dict,
          inplace=True)

# print Data frame after rename columns
print(df)
