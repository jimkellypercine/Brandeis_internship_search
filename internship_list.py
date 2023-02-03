import pandas as pd
import numpy as np

# Load the Excel file into a Pandas dataframe
df = pd.read_excel('Internship_list.xlsx')

# Display the first 4 rows of the dataframe
print(df.head(7))


f= open("README.md", "a")
f.write(df.to_csv())
f.close()
#np.savetxt('./README.md', df.values)
