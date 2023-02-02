import pandas as pd

# Load the Excel file into a Pandas dataframe
df = pd.read_excel('Internship_list.xlsx')

# Display the first 4 rows of the dataframe
print(df.head(4))
