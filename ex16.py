from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit return.")

input('?')

print("Opening the file...")
target = open(filename, 'w')
# when 'w' is used in open(), truncate() is not necessary,
# for in this mode, the file will be truncated if it already exists.

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# target.write(line1)
# target.write('\n')
# target.write(line2)
# target.write('\n')
# target.write(line3)
# target.write('\n')

target.write("%r\n%r\n%r" % (line1,line2,line3))

print("And finally, we close it.")
target.close()