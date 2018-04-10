# people = 30
# cars = 40
# buses = 15

# make three variables and binds them to some integers
people = 290
cars = 28
buses = 89


# make comparisons using if-clause
# if cars > people is true, implement its following chunk
if cars > people:
    print("We should take the cars.")
# if cars < people is true, implement its following chunk
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if buses > cars:
    print("That's too many buses.")
elif buses < cars:
    print("Maybe we could take the buses.")
else:
    print("We still can't decide.")

if people > buses:
    print("Alright, let's just take the buses.")
else:
    print("Fine, let's stay home then.")

if cars > people or people < buses:
    print("Oh, I really can't decide.")

if cars > people or people != buses:
    print("Oh, I really can't decide.")