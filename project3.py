# Import math Library
import math
def square(a):
    return a
result= math.sqrt(25)

print(result)

2
def largest(numbers):
    return max(numbers)

print(largest([2,22,10,20]))

3
def average(*numbers):
    return sum(numbers)/ len(numbers)
   


result= average(1,2,3,5,6,7)
print(result)

4
def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))

