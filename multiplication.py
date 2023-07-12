
n=int(input("Enter a number for multiplication table: "))
r=int(input("Enter the range to print: "))

for i in range(r+1):
    print(str(i) + " x " + str(n) + " = " + str(i*n))