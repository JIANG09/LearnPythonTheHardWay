def while_function(x, j):
    i = 0
    numbers = []

    while i < j:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + x
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    return numbers


numbers_1 = while_function(7, 10)

print("The numbers: ")

for num in numbers_1:
    print(num)

