#py the hard way
#ex39

# - *- coding: utf- 8 - *-

# create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',	
	'Florida': 'FL', 
	'California': 'CA', 
	'New York': 'NY', 
	'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Miami'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
	print(f"{abbrev} has the city {city}")
	
# print state abbreviation and city
print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} is abbreviated {abbrev}")
	print(f"and has the city {cities[abbrev]}")
	
print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')
if not state:
	print("Sorry, no Texas")
	
# get a city with a default value
city = cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is: {city}")


print("Enter the abbreviation to find city in the state")
print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{abbrev}")
print('-' * 10)
state_abbrev = input("< ")
print('-' * 10)
print(f"State {state_abbrev} has city {cities[state_abbrev]}") 