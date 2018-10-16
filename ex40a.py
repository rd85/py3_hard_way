#py the hard way
#ex40a

# - *- coding: utf- 8 - *-

mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

def apple():
	print("I AM APPLES!")
	
'''
import ex40a
ex40a.apple() #will return print statement
'''
	
tangerine = "Living reflection of a dream"

'''
import ex40a
print(ex40a.tangerine) #will return value of the variable tangerine
'''

class MyStuff(object):
	
	def __init__(self):
		self.tangerine = "And now a thousand years between"
	
	def apple(self):
		print("I AM CLASSY APPLES!")

thing = MyStuff()
thing.apple()
print(thing.tangerine)