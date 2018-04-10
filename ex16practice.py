from sys import argv

script, filename = argv

print("We're going to read %r." % filename)
print("If you don't want that, hit CTRL^C.")
print("If you do want that, hit RETURN.")

input('The file is coming ... ')
target = open(filename, 'r')

target.close()