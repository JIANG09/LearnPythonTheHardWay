from sys import argv

script, filename = argv

print(f"We're going to open {filename} file.")
print("If you don't want that, hit CTRL^C.")
print("If you do want that, hit RETURN.")

input("So your choice is: ")
print("The file is coming...")
target = open(filename)
print(target.read())

target.close()
