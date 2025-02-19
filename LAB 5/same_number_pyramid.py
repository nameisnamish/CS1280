n = int(input("Enter the number of rows: "))
int = input("Enter the integer to use: ")

for i in range(1, n+1):
    print(" " * (n - i) + int * (2 * i - 1))
