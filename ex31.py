print("""You enter a dark room with two doors. 
Do you go through door #1 or door #2? or door #X?""")

door = input("> ")

if door == "1":
    print("There is a giant bear here eating a cheese cake. What do you do?")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your leg off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello. Good job!")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

elif door == "X" or door == "x":
    print("""There is a treasury map in this room.
Choose the button and we will see!""")
    print("Left.")
    print("Right.")

    button = input("> ")

    if button == "Left" or button == "left":
        print("The treasure map is in the box underground! Get it and find the treasure!")
        print("You will become very very rich!")
    elif button == "Right" or button == "right":
        print("Such a bad luck! You find nothing!")
    else:
        print("Invalid input!")

else:
    print("You stumble around and fall on a knife and die. Good job!")
