print("-----------SPECIAL CHARS IN PYTHON----------")
# \n  \\  \'  \"  \a  \b  \f  \r  \t  \v  \0  \xhh  \ooo  \N{id}  \uhhhh  \Uhhhhhhhh  and else
# \n - line break
# \t - gorizontal tabulation
# \v - vertical tabulation
# \f - change format
# \b - backspace emulation and so on...
test = "cat\n"
print(r"test = cat\n", "len(test) = ", len(test), "because \"\\n\" is 1 of special chars", sep=" ")

# HOW TO ESCAPE SPECIAL CHARACTERS WHEN WE USE IT IN STRINGS?
print("-----------BACKSLASH PROTECTION----------")
print("panda\needs fruits")  # panda
                             # eeds fruits
print("panda\\needs fruits") # panda\needs fruits

print("-----------RAW STRING PROTECTION----------")
# EX: Path to a file
path = r"D:\\Python\north\test.py"
print(path)  # D:\\Python\north\test.py

print("-----------BAD STYLE PROTECTION FOR QUOTATION MARKS----------")
print("Wine 'Summer fruits'")  # In this case we used mix of single and double quotation marks