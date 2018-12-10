tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
'''

'''print(tabby_cat)'''  # ''' is used to comment out pieces of codes.
print(tabby_cat)
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
\t* {}
\t* {}
\t* {}\n\t* {}
"""

print(fat_cat.format(tabby_cat, backslash_cat, grass_cat, persian_cat))

how_tall = " 6'2\" "
how_tall2 = ' 7\'2" '
print(f"I'am {how_tall} tall.")
print(f"I'am not {how_tall2} tall.")
my_tall = "\tI'am {} tall \n\tbut not {} tall."
print(my_tall.format(how_tall, how_tall2))
