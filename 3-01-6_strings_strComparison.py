# STRING is an important data type in python
s1 = "CungFU"
s2 = 'Panda'
print(s1, s2, "\n--------------")  # simple strings
sLong1 = '''In addition to the standard library,
there is an active collection of hundreds of thousands of components'''
print(sLong1, type(sLong1), sep='    ')  #  first variant of long string

sLong2 = """(from individual programs and modules to packages and entire application development frameworks),
available from the Python Package Index.   """
print(sLong2, type(sLong2), "\n-------------")  #  second variant of long string

# STRING CONCATENATION
sIlike = 'I like'
sPython = 'Python'
print(sIlike + "..." + sPython + "...it's concatenation" + "\n--------------")

# STR() modified accept argument and returns string
print(type(str(5.6)))  #  <class 'str'>

# OPERATOR '*' makes str by multiplicating substring
strMultiple = "txt " * 5
print(strMultiple)  #  txt txt txt txt txt

# LEN() returns length of string
print("strMultiple length = ", len(strMultiple))  # 20

# ORD() accept symbole, returns ASCII code
# CHR() accept ASCII code, returns symbole
print(ord('K'), chr(75))  # 75 K

# ----------------PYTHON STRING COMPARISON----------------------

# OPERATOR 'IN' returns True if substring is in string
print('ab' in 'abdfd')  #  True

# OPERATORS '==', '!='
strHello = "Hello"
print(strHello, "== Hello", strHello == "Hello")  # Hello == Hello True

# OPERATORS '>', '<', '>=', '<='
print('\"cat\" > \"cit\"?', "cat" > "cit")  # False
# Operator compares symbols in two strings from first to last one by one using ASCII-code table
# 1. 'c' = 'c' go on!
# 2. 'a' > 'i' False bingo! -> operator returns False
# 3. next symbols ignored
