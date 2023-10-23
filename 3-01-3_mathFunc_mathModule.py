# PYTHON OWN MATH FUNCTIONS
# ABS() accept numeric, returns it's module
print(abs(-5.6))  # =5.6

# MIN() accept different numbers, return minimal
print(min(1, 0, -5, 6.7, -8.34))  # =-8.34
var1, var2 = 78, 12
print(min(var1, var2))  # =12

# POW() accept 2 parameters: numeric and degree, return: result of exponentiation
print(pow(2, 3))  # 2^3=8

# ROUND() accept numeric, return type integer round numeric
print(round(5.43), round(3.12), round(7.499), round(7.5))  # = 5 3 7 8
print(type(round(6.5)))  # <class 'int'>
print(round(7.3411, 2))  # 7.34
print(round(7.3411, -1))  # 10.0

# Python makes it easy to call one function from another
print(max(1, 2, abs(-5)))  # =5

# ADDITIONAL (OPTIONAL) MODULE MATH
import math
print("-------import math--------")
print(math.ceil(5.21))  # =6 round number to bigger integer
print(math.floor(7.88))  # =7 round number to smaller integer
print(math.factorial(4))  # 1*2*3*4 = 24 calculate and return numeric factorial
print(math.trunc(4.3344))  # =4 delete float numeric part after '.' and return integer numeric
print(math.log2(8))  # 3.0
print(math.log10(100))  # 2.0
print(math.sqrt(16))  # 4.0
print(math.pi, math.e)  # 3.141592653589793 2.718281828459045
print(math.log(2.7))  # 0.9932517730102834 natural logarithm
print(math.log(2.7, 3))  # 0.9040967257106154 logarithm with base 3
