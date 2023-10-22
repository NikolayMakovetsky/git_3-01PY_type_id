#Assign Operator '=' creates a link between variable and data storage
#If in programm we have no links to storage object, it will be deleted by garbage cleaner
a = 7
b = 8
a = b
print(a, b) #storage object with number = 7 deleted, because we have no links to it
#So, now we nave one object with number = 8 and two links to it

#Strict typing

#Dynamic typing
var_a = "Panda" #Variable creates when we assign it's first value
print(var_a)