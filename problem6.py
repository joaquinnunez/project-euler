# Sum square difference https://projecteuler.net/problem=6

n = 100
sum_of_squares = (n * (n + 1) * (2 * n + 1)) / 6
square_of_sum = ((n * (n + 1)) / 2) ** 2
diff = square_of_sum - sum_of_squares
print("The difference is {}".format(diff))
