from sys import argv

#read the WYS section from how to run this
script, first, second, third = argv

#ok so argv reads the arguments when i run the script
# so i run it now like:
# python ex13.py one two three
# and the ex13.py one tho three are the args i unpack from argv

print("script ", script)
print("first ", first)
print("second ", second)
print("third", third)

data = input("Some more data: ")
print(data)
