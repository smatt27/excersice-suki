"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = None
def is_sub_or_sup(small, big):
    if len(small) > len(big):
        return False 
    for n in range(len(big)-len(small)+1):
        if big[n:n + len(small)] == small:
            return True 
    return False 

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif not list_one or not list_two:
        if not list_one:
            return SUBLIST
        else:
            return SUPERLIST
    elif len(list_one) > len(list_two):
        if is_sub_or_sup(list_two, list_one):
            return SUPERLIST
    elif len(list_two) > len(list_one):
        if is_sub_or_sup(list_one, list_two):
            return SUBLIST
    else:
        return UNEQUAL
    
