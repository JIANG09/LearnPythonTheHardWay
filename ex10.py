tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

'''print(tabby_cat)'''  # ''' is used to comment out pieces of codes.
print(persian_cat)
print(backslash_cat)
print(fat_cat)


'''while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print("%s\r" % i)'''

# Practice
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
grass_cat = "grass"

fat_cat = """
I'll do a list:
\t* %s
\t* %s
\t* %s\n\t* %s
"""

print(fat_cat %(tabby_cat, backslash_cat, grass_cat, persian_cat))

how_tall = " 6'2\" "
how_tall2 = ' 6\'2" '
print("I am %r tall" % how_tall)
print("I am %s tall" % how_tall)
print("I am %r tall" % how_tall2)
print("I am %s tall" % how_tall2)

