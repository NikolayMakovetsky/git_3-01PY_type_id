#Assign Operator '=' creates a link between variable and data storage
#If in programm we have no links to storage object, it will be deleted by garbage cleaner
a = 7
b = 8
a = b
print(a, b) #storage object with number = 7 deleted, because we have no links to it
#So, now we nave one object with number = 8 and two links to it

#Strict (hard) typing

#Dynamic typing
var_a = "Panda 2" #Variable creates when we assign it's first value
print(var_a)

#Cascading assignment
c = d = f = 0
print(c, d, f)

#id() function returns variable linked object identificator
print(id(var_a))

#type() function returns variable linked data type
print(type(var_a))

#Variable names ALLOWD:
#First symbol from a...z \ A...Z also symbol '_'
#form Second to last symbols also we can use numbers 0...9

#Variable names NOT ALLOWD:
#Python Console
#help()
#keywords