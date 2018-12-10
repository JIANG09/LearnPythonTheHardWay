# make three variables and binds them to some integers
people = 300
cars = 4005
trucks = 1555


# make comparisons using if-clause
# if cars > people is true, implement its following chunk
if cars > people:
    print("We should take the cars.")
# if cars < people is true, implement its following chunk
elif cars < people:
    print("We should not take the cars.")
# if none of the above are true, implement the following chunk
else:
    print("We can't decide.")

# if trucks > people is true, implement its following chunk
if trucks > cars:
    print("That's too many trucks.")
# if trucks < cars is true, implement its following chunk
elif trucks < cars:
    print("Maybe we could take the trucks.")
# if none of the above are true, implement the following chunk
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

if cars <= people and people >= trucks:
    print("Let's go to see a movie!")

if cars > people or trucks < cars:
    print("What a good day today!")
