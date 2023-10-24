# STRING is a symbol collection, each element has own number
# STRING is a massive/list of symbols
str = "Hello Python"
print(str)
# H   e    l   l  o  _  P  y  t  h  o   n
# 0   1    2   3  4  5  6  7  8  9  10  11
# -12 -11 -10 -9 -8 -7 -6 -5 -4 -3  -2  -1

# HOW TO FIND SYMBOL IN STRING?
print("------Find symbol in string------------")
print(str[-4])              # t
print(str[len(str) - 1])    # n
print("panda"[3])           # d

# STRING SLICE [start:stop]
print("-----------Slices------------")
print(str[1:5])    # ello
print(str[8:])      # thon
print(str[:3])      # Hel
print(str[:])       # Hello Python (full slice) result object has the same id
print(str[2:2])     # empty slice
print(str[-2:2])    # empty slice
print(str[2:-2])    # llo Pyth // slices works only from left to the right

# STRING SLICES WITH 'STEP' [start:stop:step] BY DEFAULT: step = 1
print("---------Slices with parameter step---------")
print(str[2:10:2])  # loPt // l(2)o(4)P(8)t(10)
print(str[::-1])    # nohtyP olleH // IDEA how to REVERSE STRING // if step < 0 slice starts from last element!!!

# STRING IS UNCHANGEABLE DATA TYPE
#str[0] = 'Y'  # TypeError: 'str' object does not support item assignment

# BUT HOW TO CHANGE STRING? TO CREATE NEW ONE!
str2 = "Y" + str[1:]
print(str2)     # Yello Python

