#py the hard way
#ex18

# - *- coding: utf- 8 - *-

def print_two(*args):
	arg1, arg2 = args
	print(f"Arg1 : {arg1}; Arg2 : {arg2}")

def print_two_again(arg1, arg2):
	print(f"Arg1 : {arg1}; Arg2 : {arg2}")
	
def print_one(arg1):
	print(f"Arg1: {arg1}")
	
def print_none():
	print("I got nothin'.")

print_two("Tracer", "Bullet")
print_two_again("Jon", "Snow")
print_one("First!")
print_none()