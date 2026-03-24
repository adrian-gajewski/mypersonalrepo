input=input("Provide the sentence to reversed: ")

lenght= len(input)

reversed=""
i=lenght-1
while i >=0:

    reversed=reversed+input[i]
    i=i-1

print("Lenght is: ",len(input))

print("Last char is: ",input[lenght-1])
print("reversed is: ",reversed)