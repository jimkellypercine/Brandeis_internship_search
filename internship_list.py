import pandas as pd

# Load the Excel file into a Pandas dataframe
df = pd.read_excel('Internship_list.xlsx')

# Display the first 4 rows of the dataframe
print(df)
df = df.reset_index(drop=True)
df.index = df.index + 1

UDRS = ["Yalda Mauj", "Jimkelly Percine", "Gabrielle Pile", "Gianna Everette", "Sydney Cohen"]

print(df)

#load the dataframe into a markdown file
f= open("README.md", "w")
markdown = '![](images/brandeispic.png)' 
f.write(markdown)
f.write("\n \n BRANDEIS COSCI HANDBOOK: https://docs.google.com/document/d/1skDckhZJi6OQxjraKNVEZfxflTE4Jy8kxCJtpNu3O1Y/edit?usp=gmail \n" + "\n")
f.write(" \n CURRENT UDRS \n " + "\n".join(["- " + UDRS for UDRS in UDRS]))
f.write("\n \n Connect with Contributors\n https://docs.google.com/document/d/1XWu8NFlqvPPQSOIbt93K7tdSejl2mA1KmV7HSjAZLMs/edit?usp=sharing")
f.write("\n \n List of internships within the COSI Department \n" + df.to_markdown(floatfmt=".2f"))
f.close()
