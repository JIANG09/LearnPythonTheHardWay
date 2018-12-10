ten_things = "Apple Oranges Crows Telephone Light Sugar"

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

for item in more_stuff:
    if len(stuff) != 10:
        stuff.append(item)

print(stuff)
print(f"There's {len(stuff)} items now.")


