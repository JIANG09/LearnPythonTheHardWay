# create a variable named types_of_people and sets it to 10
types_of_people = 10
# create a variable named x and sets it to formatted string with a string put inside
# 1st place where a string is put inside a string.
x = f"There are {types_of_people} types of people"

# create two variables and set them to different strings
binary = "binary"
do_not = "don't"

# create a variable named y and sets it to a formatted string
# 2nd place where a string is put inside a string.
y = f"Those who know {binary} and those who {do_not}."

# print out x and y
print(x)
print(y)

# print the formatted string which has a variable
# 3rd and 4th places where a string is put inside a string.
print(f"I said: {x}")
print(f"I also said: '{y}'")

# create a variable named hilarious and set it to a boolean value False
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# the 5th place where a string is put inside a string
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

