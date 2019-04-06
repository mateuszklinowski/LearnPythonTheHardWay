days = "Mon Tue Wed Thu Fri Sat Sun"

# so \ is same as in JS escape chat and then next is interpreted "diffrent"
months = "Jan\nFeb'nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are days: ", days)
print("Months: ", months)


print("MMMMMM \"\"\" ")

# \n still work inside this
print("""
There's something going on here.
With the three double-quotes.\n
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.


OK so this is multi line text, It keep line breaks by itself ;)
""")
