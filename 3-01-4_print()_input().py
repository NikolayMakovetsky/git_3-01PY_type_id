# PRINT() output data to console
# parameter SEP set type of element that will separate parts of output data
# parameter END set end element of output data
print("hello", "world", sep=" ! ", end=" ")
print("|| sep=\" ! \", end=\" \"")
print("in example default end element end=\"\\n\" changed to element \" \"")

# F-LINES format output
x = 5.76
y = -8
print(f"Actual coordinates of point | x: {x}, y: {y}")  # x: 5.76, y: -8

# INPUT() take string information from users keyboard
print("Input integer numeric:", end=" ")
a = int(input())  # We retype string information to integer and save link to it in variable 'a'
print(f"Your choice: {a}, {type(a)}, \n----------------------")

# Ex: how to insert 2 parameters in 1 line
print("Insert sides of rectangle:", end=" ")
a, b = map(float, input().split())
print(a, type(a), b, type(b), "\n----------------------")

