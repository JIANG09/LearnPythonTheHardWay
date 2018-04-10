print("You enter a dark room with three doors. Do you go through door #1 or door #2? or door #3?")

door = input("> ")

if door == "1":
    print("There is a giant bear here eating a cheese cake. What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    print("3. Change yourself into a bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your leg off. Good job!")
    elif bear == "3":
        print("You start a fight with the bear. Fighting!")
    else:
        print("Well, doing %s is probably better. Bear runs away." % bear)

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello. Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck. Good job!")

elif door == "3":
    print("""There is sword in this room.""")
    print("1. Take the sword and go back to door #1.")
    print("2. Take the sword and leave the room as soon as possible.")
    print("3. Leave the sword and leave the room as soon as possible.")

    sword = input("> ")

    if sword == "1":
        print("Congratulation! The room is a kingdom. You conquer the bear and becomes the ruler!")
    elif sword == "2":
        print("The sword is priceless. You become the richest man in the town.")
    elif sword == "3":
        print("Pity! There is a bear in this room and you have nothing to duel with him.")
    else:
        print("Leave this room!")

else:
    print("You stumble around and fall on a knife and die. Good job!")
