from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Coping from {from_file} to {to_file}")


#how to write this in 1 line1
#in_file = open(from_file)
#indata = in_file.read()

#solution:

#indata = open(from_file).read()

#print(f"The input file is {len(indata)} bytes long")

#print(f"Does output file exist? {exists(to_file)}")
#print("Ready, press key to continue, CTRL-C to abort")

#input(" ? ")

#open(to_file,'w').write(indata)

#print("Alright, all done")


#One line implementation
open(to_file, 'w').write(open(from_file).read())
