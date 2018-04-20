# 3. Write a Python program to compute the value of e(2.718281827...) using infinite series.
import math

def exp(num):
    return sum(1 / float(math.factorial(i)) for i in range(num))

num = int(input("Enter the iterations : "))
for i in range(num):
    print(exp(i))
