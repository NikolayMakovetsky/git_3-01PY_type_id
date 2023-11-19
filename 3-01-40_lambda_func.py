print("\n--------------------LAMBDA ANONYMOUS FUNCTION-------------------")
print("a function that includes only one python construction and returns one value")
print("lambda can be written only in one line")
print("lambda has automatical return operator inside itself")
print("in lambda we can't use operator '=': lambda a : a = 1 -> ERROR!")
print("inside lambda we can create an object by using incoming parameters and Global variables")
print("""\n-----------------------SYNTAX--------------------------
keyword           if we need it               
   ---     --------------------------          ---
lambda parameter1, parameter2...parameterN : command
""")

print("\n--------------USE VARIABLE TO SAVE LAMBDA FUNCTION IN MEMORY----------------")
s = lambda a, b : a + b
print(f"s = lambda a, b : a + b  ->  {s = }")
print(f"s = lambda a, b : a + b  ->  {s(1, 2) = }")

print("\n------------USE LAMBDA IN DIFFERENT PYTHON CONSTRUCRIONS-----------")
a = [1, lambda a : a ** 2, 3]
print(f"a = [1, lambda a : a ** 2, 3]   ->   {a = }")
print(f"a = [1, lambda a : a ** 2, 3]   ->   {a[1] = }")
print(f"a = [1, lambda a : a ** 2, 3]   ->   {a[1](3) = }  // () - calling operator")

print("\n-------------HOW TO MODIFY VARS IN LIST IN DIFF WAYS BY USING ONE FUNCTION?-----------")


def get_modify(a, fctn = None):
    if fctn:
        for x, y in enumerate(a):
            a[x] = fctn(y)


lst = [1, 2, 3, 4, 5]
print(f"{lst = }\n")
get_modify(lst, lambda x : x * 0 if x > 2 else x)
print(f"{lst = }      // get_modify(lst, lambda x : x * 0 if x > 2 else x)")
get_modify(lst, lambda x : x + 3)
print(f"{lst = }      // get_modify(lst, lambda x : x + 3)")
get_modify(lst, lambda x : True if x == 5 else x)
print(f"{lst = }   // get_modify(lst, lambda x : True if x == 5 else x)")
get_modify(lst, lambda x : 5)
print(f"{lst = }      // get_modify(lst, lambda x : 5)")
