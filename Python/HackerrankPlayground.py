# This code will create a simplified fruit salad with the provided fruits
fruits = ['apple', 'banana', 'cherry', 'date']
fruits_in_salad = ""

index = 0
# TODO: Create a while loop that assembles a string of fruit names separated by spaces, without adding a space after the last fruit
# Hint: Consider using a conditional to determine when to add a space
while index < len(fruits):
    if index == (len(fruits))-1:
        fruits_in_salad=fruits_in_salad+fruits[index]
        index+=1
    else:    
         fruits_in_salad=fruits_in_salad+fruits[index]+" "
         index+=1



print(fruits_in_salad)  # Output the fruits in the salad
with open(r"C:\Users\tolka\Desktop\output.txt","w") as File1:
    File1.write(fruits_in_salad)
     
