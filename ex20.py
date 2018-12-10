from sys import argv

script, input_file = argv


def print_all(f):  # define a function called print_all, with one parameter
    print(f.read())  # the function prints out the content read of parameter that is passed to the function.


def rewind(f):  # define a function call rewind, with one parameter
    f.seek(0)   # the function calls seek() method which goes back 0 byte of the file


# define a function called print_a_line, with two parameter
def print_a_line(line_count, f):
    print(line_count, f.readline(), end='')  # print out line_count and current line of the passed file


current_file = open(input_file)
# call open() on argument given to the script and binding it to a variable

print("Now let's print the whole file: \n")

print_all(current_file)  # call print_all with a passed parameter current_file

print("Now let's rewind, kind of like a tape.")

rewind(current_file)  # call rewind with a passed parameter current_file

print("Let's print three lines:")

# current_line = 1
current_line = 1
# call print_a_line with two passed parameters
print_a_line(current_line, current_file)

# current_line = 2
current_line += 1
# call print_a_line with two passed parameters, one of which is adding one to itself
print_a_line(current_line, current_file)

# current_line = 3
current_line += 1
# call print_a_line with two passed parameters, one of which is adding one to itself
print_a_line(current_line, current_file)
