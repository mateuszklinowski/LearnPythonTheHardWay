from sys import argv

script, file = argv

def print_all(file):
    print(file.read())

def rewind(file):
    file.seek(0)

def print_a_line(line_count, file):
    print(line_count, file.readline(), end="")

current_file = open(file)

print_all(current_file)
rewind(current_file)

current_line = 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
