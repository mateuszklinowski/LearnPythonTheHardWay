types_of_people = 10
x = f"This is use case for types_ {types_of_people}."

binary = "binary"
do_not =  "don't"
y = f"Those who {binary} and those who {do_not}"

print(x)
print(y)

print(f"test this print: {x}")

hilarious = False
joke_evaluation = "Isn't that so funny?! {} {}"

print(joke_evaluation.format(hilarious, hilarious))
