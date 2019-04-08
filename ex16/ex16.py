from sys import argv

script, filename = argv

print(f"We are going to erase {filename}")
print("To stop that hit CTRL-C (^C)")
print("To continue press ENTER")

input("> ?")

print("Opening the file...")
target = open(filename, 'w')

#seems like Opening with 'w' option turncate by default
#print("Turncating the file...")
#target.truncate()

print("Enter new file content:")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("writing lines to file...")

target.write(f"{line1}\n{line2}\n{line3}\n")

print("Closing file...")
target.close()

print("New file content: ")
print(open(filename).read())
