#Get user input
num = int(input("Enter a number : "))

#print the multiplication table
print(f"Multiplication table of {num} :")
for i in range(1,11): #Loop from 1 to 10
    print(f"{num} X {i} = {num * i}")
    