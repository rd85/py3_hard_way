#py the hard way
#ex25

# - *- coding: utf- 8 - *-

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split()
    return(words)

def sort_words(words):
    """This function will sort the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    return(word)
	
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    return(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
	
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

sentence = "All good things come to those who wait."
words = break_words(sentence)
print(words)

sorted_words = sort_words(words)
print(sorted_words)
print(print_first_word(words))
print(print_last_word(words))

print(words)
print(print_first_word(sorted_words))
print(print_last_word(sorted_words))
print(sorted_words)

sorted_words = sort_sentence(sentence)
print(sorted_words)
print(print_first_and_last(sentence))
print(print_first_and_last_sorted(sentence))
