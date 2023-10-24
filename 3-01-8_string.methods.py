# METHOD is an built-in object function in Python
# Object.method(arguments)
msg = "abrakadabra"

print("----.COUNT()---------.REPLACE()-------------")

# .COUNT(sub, start, end) returns number of repeats substring 'sub' in string
print(msg.count("ra", 1 , 11))  # 2 "ra" in "brakadabra"

# .REPLACE(old symbol, new symbol, count) // count = 1 maximum one replacement // count = -1 no limit replacements
print(msg.replace('a', 'o', -1))  # obrokodobro
print(msg.replace('a', 'o', 2))  # obrokadabra

print("----.SPLIT()----.JOIN()-----.UPPER()----.LOWER()-----------")

# .SPLIT(sep="", maxsplit = -1) returns collection of substrings maked from basic string // maxsplit = -1 no limit of separations
print("Ivanov Ivan Ivanovich".split(" ", 1))  # ['Ivanov', 'Ivan Ivanovich']
digs = "1, 2,  3,4,5   6,"
digsList = digs.replace(" ", "").split(",")
print(digsList)  # ['1', '2', '3', '4', '56', '']

# .JOIN() return one joined string
digsJoined = " ".join(digsList)
print(digsJoined, type(digsJoined))  # 1 2 3 4 56  <class 'str'>

# .UPPER() .LOWER() change letters register
print(msg.upper(), type(msg.upper))  # ABRAKADABRA <class 'builtin_function_or_method'> // msg.upper is a link to the object-function
print(msg.lower(), type(msg.lower))  # abrakadabra <class 'builtin_function_or_method'> // msg.lower is a link to the object-function

print("----.FIND()----.RFIND()-----.INDEX()----------------")

# .FIND(sub, start, end) finds first sub-element in string and returns it's ID // else returns -1 // it goes from left to the righr
print(msg.find("bra", 2, 12), end="  ")  # 8 abrakadaBRA
print(msg.find("bro"), end="  ")          # -1 (no finded

# .RFIND(sub, start, end) works the same like .FIND but do it from RIGHT TO THE LEFT !!!
print(msg.find("bra"), end="  ")  # 1 aBRAkadabra .FIND
print(msg.rfind("bra"), end="  ")  # 8 abrakadaBRA .RFIND

# .INDEX(sub, start, end) works the same like .FIND but RETURNS ERROR IF THERE IS NO SUBSTRINGS !!!
print(msg.index("bra"))  # 1
#print(msg.index("bb"))  # ValueError: substring not found

print("----.ISALPHA()----.ISDIGIT()-----.RJUST-------.LJUST-----")

# .ISALPHA() .ISDIGIT() returns True / False
print("\"HELLow\".isalpha()", "HELLow".isalpha())        # True
print("\"HELLow!\".isalpha()", "HELLow!)".isalpha())     # False
print("\"234\".isdigit()", "234".isdigit())              # True
print("\"2.34\".isdigit()", "2.34".isdigit())            # False

# .RJUST(width, fillchar = "0") returns new string with added letters to the LEFT SIDE
# .LJUST(width, fillchar = "0") returns new string with added letters to the RIGHT SIDE
bankNumber = "34562"
print(".rjust", bankNumber.rjust(10, "0"))  # 0000034562
print(".ljust", bankNumber.ljust(10, "0"))  # 3456200000
print(".rjust(4)", bankNumber.rjust(4, " "))   # 34562 // because len(bankNumber) = 5, but 4 < 5

# lstrip, rstrip and strip remove characters from the left, right and both ends of a string respectively.
# By default they remove whitespace characters (space, tabs, linebreaks, etc)
test = "    a b c    "
print("----------strip test 1--------\n", test)   # "    a b c    "
print(test.strip())  # "a b c"
print(test.lstrip())  # "a b c    "
print(test.rstrip())  # "    a b c"

test = "abc a b c abc"
print("----------strip test 2--------\n", test)  # "abc a b c abc"
print(test.strip("cab"))  # " a b c "
print(test.lstrip("cab"))  # " a b c abc"
print(test.rstrip("cab"))  # "abc a b c "

test = "abc a b c abc"
print("----------strip test 3--------\n", test)  # "abc a b c abc"
print(test.strip("c ab"))  # ""
print(test.lstrip("c ab"))  # ""
print(test.rstrip("c ab"))  # ""

test = "abc ab bc cb bbbbbbbb FAQ a b c aa bb cc abc"
print("----------strip test 4--------\n", test)  # "abc ab bc cb bbbbbbbb FAQ a b c aa bb cc abc"
print(test.strip("c ab"))  # "FAQ"
print(test.lstrip("c ab"))  # "FAQ a b c aa bb cc abc"
print(test.rstrip("c ab"))  # "abc ab bc cb bbbbbbbb FAQ"