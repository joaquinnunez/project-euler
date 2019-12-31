# Maximum path sum II, https://projecteuler.net/problem=67
#    3
#   7 4
#  2 4 6
# 8 5 9 3
# 
# 8 + 2 = 10
# 2 + 5 = 7
# bigger? 10
# 
# row = [10]
# 
# 4 + 5 = 9
# 4 + 9 = 13
# bigger? 13
# 
# row = [10, 13]
# 
# 9 + 6 = 15
# 6 + 3 = 9
# bigger? = 15
# 
# row = [10, 13, 15]
# 
# 
#    3
#   7 4
# 10 13 15
# 
# 10 + 7 = 17
# 7 + 13 = 20
# bigger? 20
# 
# row = [20]
# 
# 4 + 13 = 17
# 4 + 15 = 19
# bigger? 19
# 
# row = [20, 19]
# 
# 
#   3
# 20 19
# 
# 20 + 3 = 23
# 19 + 3 = 22
# bigger? = 23
# 
# Result = 23
