ten_things = "Apple Oranges Crows Telephone Light Sugar"

print("Wait there's not 10 things in that list, let's fix that.")

# split(ten_things, ' '), use ' ' split ten_things to make a list
# call split on ten_things / call split with arguments ten_things and ' '
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    # pop(more_stuff)
    # call pop on more_stuff / call pop with argument more_stuff
    next_one = more_stuff.pop()  
    print("Adding: ", next_one)
    # append next_one to stuff append(stuff, next_one)
    # call append on stuff / call append with arguments stuff and next_one
    stuff.append(next_one)  
    print(f"There's {len(stuff)} items now.")


print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])  # whoa! fancy!
# stuff.pop(0) is pop(stuff, 0)
# call pop with argument 0 on stuff/ call pop with arguments stuff and 0
print(stuff.pop(0))
# ' '.join(stuff) is join(' ', stuff)
# call join with argument stuff on ' '; call join with arguments ' ' and stuff
print(' '.join(stuff))
print('#'.join(stuff[3:5]))   # super stellar!  join('#', stuff[3:5])
# join('*', stuff[:])
# call join with argument stuff[:] on * / call join with arguments * and stuff[:]
print('*'.join(stuff[:]))

