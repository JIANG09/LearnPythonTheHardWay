from sys import argv

script, input_file = argv


def print_all(f):  # define a function called print_all, with one parameter
    print(f.read())  # the function prints out the content read in parameter that is passed to the function.


def rewind(f):  # define a function call rewind, with one parameter
    f.seek(0)   # the function calls seek()method which goes back the the 0 byte of the file


def print_a_line(line_count, f):  # define a function called print_a_line, with two parameter
    print(line_count, f.readline())  # print out line_count which is passed to the function and line of the passed file


current_file = open(input_file)
# call the function open() on argument given to the script and binding it to a variable

print("Now let's print the whole file: \n")

print_all(current_file)  # call the function print_all with a passed parameter

print("Now let's rewind, kind of like a tape.")

rewind(current_file)  # call the function rewind with a passed parameter

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)  # call the function print_a_line with two passed parameters

current_line = current_line + 1  # add one to variable current_line
print_a_line(current_line, current_file)
# call the function print_a_line with two passed parameters, one of which is adding one to itself

current_line = current_line + 1  # add one to variable current_line
print_a_line(current_line, current_file)
# call the function print_a_line with two passed parameters, one of which is adding one to itself