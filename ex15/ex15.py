from sys import argv

script, filename = argv

# open a file using a file type,
# returns a file object

txt = open(filename)
print(txt)
print(f"Here is file name {filename}")
print(txt.read())

#this close file`
txt.close()

# print("Type filename again:")
# file_again = input("> ")
#
# txt_new = open(file_again)
#
# content = txt_new.read()
# txt_new.close()
# print(content)
