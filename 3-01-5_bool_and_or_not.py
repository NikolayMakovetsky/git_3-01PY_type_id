# LOGIC TYPE BOOL
# Bool type variable can be: TRUE or FALSE
a, b = 2, 4
res = a > b
print(res, type(res), res + 2.4, type(res + 2.4))  # False <class 'bool'> 2.4 <class 'float'>
# Advice: be careful with bool variable, because it's possible unnoticed to change type 'bool' to 'int' or 'float'

# COMPRASION OPERATORS >, <, <=, >=, ==, !=

# EX: let's test if numeric division on 2
x = 8
if x % 2 == 0:
    print("numeric division on 2 \n------------------")
else:
    pass

# OPERATORS AND, OR, NOT
# PRIORITY LEVEL: OR (1), AND (2), NOT (3)
# That means 'NOT' has highest priority and it will be executed first of all

# EX: let's test if numeric is in or out of gap (2-5)
y = 4.55
if y > 2 and y < 5:
    print(f"numeric {y} in gap (2-5) \n-----------------")
else:
    pass

# EX: inverting of compose conditional operator
# REPEAT: Operator NOT has highest priority level
z = 19
if not (z % 2 == 0 or z % 3 == 0):
    print(f"{z} % 2 != 0 and {z} % 3 != 0 \n---------------")
else:
    pass

# BOOL() inverting accept different data type argument to bool type
print(bool(7.5), bool(''), bool(" "), bool(0), "\n------------")
