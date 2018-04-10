

def while_function(j, o):
    i = 0
    numbers = []

    while i < j:
        print("At the top i is %d" % i)
        numbers.append(i)

        i = i + o
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

    print("The numbers:")

    for num in numbers:
        print(num)


while_function(100, 50)


def for_function(j):
    numbers = []

    for i in range(0, j):
        print("At the top i is %d" % i)
        numbers.append(i)

        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

    print("The numbers:")

    for num in numbers:
        print(num)


for_function(8)