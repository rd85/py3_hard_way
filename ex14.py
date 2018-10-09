#py the hard way
#ex14

# - *- coding: utf- 8 - *-

from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I am {script} script")
print("I'd like to ask you a few questions.")

print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
place = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, you said {likes} about liking me.
You live in {place}. Not sure where that is.
And you have a {computer} computer. Nice!
""")