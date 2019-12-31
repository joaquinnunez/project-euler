# Factorial digit sum https://projecteuler.net/problem=20
import math

n = 100
fact = math.factorial(n)
print("Factorial of {} is {}".format(n, fact))

result = 0
while fact > 0:
  result += fact % 10
  fact /= 10

print("Sum is: {}".format(result))
