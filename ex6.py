x = 'There are %d types of people.' % 10  
# variable  x is bound to string ; the string has a format string
binary = "binary"  # a variable which is bound to a string
do_not = "don't" 
y = "Those who know %s and those who %s." % (binary,do_not)  
# it puts format string in a string by stating %s; 
# the first and second place to put a string in another string 

print(x)
print(y)

print("I said: %r." % x)  
# print out this format string
# the third place to put a string in another string 
print("I also said: '%s'." % y)
# the fourth place to put a string in another string 

hilarious = False  # a boolean value is given to variable hilarious. 
joke_evaluation = "Isn't that joke so funny?! %r"  # a format string; put a format variable to a string by using %r.  

print(joke_evaluation % hilarious)  # print put a string with a format string which is a boolean value. 

w = "This is the left side of ..."
e = "a string with a right side"

print(w + e)
# concatenation
# %r is used for debugging, while other format strings are used to present output for users.

