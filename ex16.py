#py the hard way
#ex16

# - *- coding: utf- 8 - *-

from sys import argv

script, filename = argv

print(f"We are going to erase '{filename}'")
print(f"If you do not want that, hit CTRL-C")
print(f"If you do want that, hit RETURN")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I am goingg to ask you for three lines to write to a file.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I am going to write these to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Finally, we close the file")
target.close()
