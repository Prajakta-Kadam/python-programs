# 5. Write a Python function to round up a number to specified digits.

x = float(input("Enter a number = "))
n = int(input("Enter the precision = "))
print("Original  Number: ", x)

for i in range(n+1):
    print('%.*f' % (i, x))
