
# This is my first script, that asks for your name and welcomes you.
import os;
#Clearing screen 
os.system("cls")
name=input("Name:")

my_dictionary_var = {'name': 'Alice', 'age': 25}
print('Dictionary:', my_dictionary_var) # Dictionary: {'name': 'Alice', 'age': 25}
print("Type of variable is: ",type(my_dictionary_var))

print("Is instance:", isinstance(my_dictionary_var, int))
print ("Type of variable name is:",type(name))
#testing multiline
print("First line\nSecond Line")
#String concatenation
age=24
 # Start with the name
name_and_age = name 
# Append the age as string
name_and_age =name_and_age+" "+ str(age)  

print(name_and_age)  # John Doe26

# Slicing string to print only every 2nd char  [start:stop:step]
print(name[::2])
# Replacing strings
print(name.upper().replace("A","B"))

print(name.upper())
print("First 3 letters:",name[:3])