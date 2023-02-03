import pandas as pd
import numpy as np

# Load the Excel file into a Pandas dataframe
df = pd.read_excel('Internship_list.xlsx')

# Display the first 4 rows of the dataframe
print(df.head(7))
df.reset_index(drop=True)


f= open("README.md", "w")
f.write(df.to_string())
f.close()
#np.savetxt('./README.md', df.values)
