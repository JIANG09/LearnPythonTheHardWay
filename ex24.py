print("Let's practice everything.")
print('You\'d need to know \'bout escape with \\ that do \n newlines and \t tabs.')
# \\ only \ will show
# \t: tab or indentation; \n: go on next line;
# \': ' will not be recognized as one of the pair ' '.

# This poem has multiple lines
poem = """      
the lovely world   
\n\twith logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("---------------------")
print(poem)
print("---------------------")

five = 10 - 2 + 3 - 6
print("This should be five: %d" % five)


# define a function named secret_formula; in this function, there are three mathematical operation
# and will return three values.
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
# call the function will a passed parameter start_point
# and the function will return three values which will be stored three variables beans, jars and crates.
beans, jars, crates = secret_formula(start_point)
print("With a starting point of: %d" % start_point)
print("We'd have %r beans, %d jars, and %d crates." % (beans, jars, crates))

# give another value to variable start_point
start_point = start_point / 10

print("We can also do that this way:")
# secret_formula (start_point) returns three values
# put these three values in format string which is used in print-out.
print("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))
