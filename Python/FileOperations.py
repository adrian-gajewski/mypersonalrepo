import os
os.system("cls")
filepath ="D:\GITHUB_REPO\mypersonalrepo\sales.csv"
print("Opening the file: ",filepath,"\n")
#with ensures the file is closed at the end of reading
with open(filepath,"r") as InputFile:
    
    File1=InputFile.read()
   
import_len=len(File1.splitlines())-1
print(f"Imported content of the file {import_len}: {filepath}\n")



book_titles=[]
for i, line in enumerate(File1.splitlines()):
    if i == 0:
        continue  # skip header
    
    Title = line.split(",")[2]
    book_titles.append(Title)

#Eliminating duplicates and sorting
book_titles=sorted(list(set(book_titles)))
print(f"Here are available unique book titles {len(book_titles)}: \n",book_titles)
 
#Writing to a new file about the titles
filepath2 = filepath.replace("sales.csv","sales_output.csv") 

with open(filepath2,"w") as File2:
    File2.write("These are unique titles available:\n")
    for l in book_titles:
        File2.write(l)
        File2.write("\n")