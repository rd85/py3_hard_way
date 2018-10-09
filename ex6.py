#py the hard way
#ex6

# - *- coding: utf- 8 - *-

type_of_people = 10
x = f"There are {type_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: {y}")

hilarious = False
hilarious2 = True

joke_evaluation = "Isn't that joke so funny?! {} {}"

print(joke_evaluation.format(hilarious, hilarious2))

w = "LHS.."
e = "..RHS"

print(w + e)