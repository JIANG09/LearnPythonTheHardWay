# define a function named cheese_and_crackers with two variables needed to pass to the function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheese!")  # the function will print out the number of cheese and boxes of crackers
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)  # call the function with two numbers are passed to it as parameters


print("OR, we can use variables from our script:")
# create two global variables and set them to 1o and 50
amount_of_cheese = 10
amount_of_crackers = 50

# call the function and two global variables are passed to the function as parameters
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
# call the function and give math as its parameters
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variable and math:")
# call the function; pass to function the parameters combining math and variables in parameters
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
