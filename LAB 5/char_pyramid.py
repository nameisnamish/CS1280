n = int(input("Enter the number of rows: "))
char = input("Enter the character to use: ")

for i in range(1, n+1):
    print(" " * (n - i) + char * (2 * i - 1))
