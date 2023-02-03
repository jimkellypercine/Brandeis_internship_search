import pandas as pd
import numpy as np

# Load the Excel file into a Pandas dataframe
df = pd.read_excel('Internship_list.xlsx')

# Display the first 4 rows of the dataframe
print(df)
df.reset_index(drop=True)

#load the dataframe into a markdown file
f= open("README.md", "w")
markdown = '![Alt text](brandeispic.png)' 
f.write(markdown + "\n")
f.write("COSCI HANDBOOK: https://docs.google.com/document/d/1skDckhZJi6OQxjraKNVEZfxflTE4Jy8kxCJtpNu3O1Y/edit?usp=gmail \n" + "\n")
f.write("***********************************\n       CURRENT UDRS             \n***********************************\n* Yalda Mauj                     *\n* Jimkelly Percine               *\n* Gabrielle Pile                 *\n* Gianna Everette                *\n* Sydney Cohen                   *\n***********************************\n")
f.write("List of internships within the COSI Department \n" + df.to_markdown())
f.close()
