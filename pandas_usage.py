import pandas as pd
import os
os.system("cls")
filepath ="D:\GITHUB_REPO\mypersonalrepo\sales.csv"
output_path=filepath.replace("sales.csv","output.html")
d=pd.read_csv(filepath)

print(d.columns)

#present info about table
print(d.info())
# present a data sample with 2 rows
print(d.head(2))
# extract data from particular column only
c=d[["BookTitle"]]
print(c)

#Cell value in First row and first column 
print(d.iloc[0,0])
#Save  to html 
d.to_html(output_path)