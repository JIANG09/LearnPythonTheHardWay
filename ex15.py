from sys import argv  # import argv from module sys

script, filename = argv  # set up variables script and filename

txt = open(filename)  # function open() to open the file, filename is an argument passed into the function

print("Here's your file %r:" % filename)
print(txt.read())  # method read() to read the file

print("Type the filename again:")
file_again = input('> ')  # function input() is used for user to input a filename and is given to a variable

txt_again = open(file_again)  # function open() used again

print(txt_again.read())  # method read() used tpo read the file

txt.close()
txt_again.close()

# txt = input('file:')
# print(open(txt).read())