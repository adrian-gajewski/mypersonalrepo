import os
os.system('cls')

my_set = {1, 2, 3, 4, 5, 6}
my_set.add(5)

print(my_set)

dictionary={}
i=0
while i <= 2:

    property=input("Give me Property name:")
    value=input("Give me Value:")

    # adding new entries to dictionary
    dictionary[property]=value
    i=i+1

print('Full dictionary:',dictionary)   

