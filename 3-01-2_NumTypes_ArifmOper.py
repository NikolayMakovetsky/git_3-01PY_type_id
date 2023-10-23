# There is 3 basic data types in python:
# int, float, complex
# IN FLOAT TYPE WE MUST USE '.'

a = 2 + 2  # =4 addition                 (priority 2)
b = 3 - 1  # =2 deduction                (priority 2)
c = 4 * 2  # =8 multiplication           (priority 3)
d = 9 / 2  # =4.5 division               (priority 3)
e = 9 // 2  # =4 division with rounding  (priority 3)
f = 9 % 2  # =1 division remainder       (priority 3)
g = 2 ** 3  # =8 exponentiation          (priority 4)
# OPERATIONS IN PARENTHESES !!!          (priority 5)
print(a, b, c, d, e, f, g)

# Python service variable '_' stores in Python console last calculated value

# HOW IT WORKS? ARITHMETIC OPERATION
var = 4 + 5
# var = 4 + 5 creates first object with data '4' and second object with data '5'
# then creates third object for the result of operation '9' and after this objects '4' and '5' deletes
# because there is no actual links to this objects
# RESULT: variable 'var' links to the object with data '9', so we can work with it
print(var)

# Addition integer numeric with float numeric gives float numeric
intPlusFloat = 2 + 3.0
print(intPlusFloat)  # 5.0

# Division operation always gives FLOAT result
resOfDiv = 6 / 2
print(type(resOfDiv))  # <class 'float'> even '6' and '2' are integer numerics

# Division with rounding to the least integer
posRoundDiv = 7 // 3   # =2   NOTICE: 7 / 3 = 2.3333333333333335 -> 2
negRoundDiv = -7 // 3  # =-3  NOTICE: -7 / 3 = -2.3333333333333335 -> -3
print(posRoundDiv)
print(negRoundDiv)

# Division remainder
# To understand how it works move from first value to NULL with step writes in second value
divRemPlusPlus = 9 % 5  # 9-5 = 4
divRemMinMin = -9 % -5  # -9-(-5) = -9+5 = -4
divRemPlusMin = 9 % -5  # 9-5-5 = -1
divRemMinPlus = -9 % 5  # -9+5+5 = 1
print(divRemPlusPlus, divRemMinMin, divRemPlusMin, divRemMinPlus)

# Exponentiation priority FROM RIGHT TO LEFT
expVar1 = 3 ** 8        # 3^8 = 6561
expVar2 = 3 ** 2 ** 3   # 3^(2^3) = 6561
expVar3 = (3 ** 2) ** 3   # 9^3 = 729
print(expVar1, expVar2, expVar3)

# Advice: Use correct arithmetic operations priority
arPrior1 = 27 ** 1 / 3      # 27 / 3 = 9.0
arPrior2 = 27 ** (1 / 3)    # 27^0.333333333333333333 = 3.0 # approximately correct
arPrior3 = 2 + 3 * 3 ** 2 + (4 ** (2 + 1))  # 2+3*3**2+64 = 2+3*9+64 = 2+27+64 = 93
print(arPrior1, arPrior2, arPrior3)

# ARITHMETIC OPERATORS WITH SAVING RESULT IN CURRENT VARIABLE: += -= *= /= //= %= **=
i = 0
i = i + 1
i += 1
print(i)  # 2
j = 5
j //= 3
print(j)  # 1
k = -9
k %= 4
print(k)  # 3
l = 2
l **= 3
print(l)  # 8
