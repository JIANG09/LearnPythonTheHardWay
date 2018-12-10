def house_cost(basic_fee, decoration_fee):
    print("The total cost is basic adding decoration: ", int(basic_fee) + int(decoration_fee))


print("The first way: ")
# give number directly
house_cost(100, 500)


print("The second way:")
basic = 900
decoration = 1000
# give it variables
house_cost(basic, decoration)


print("The third way:")
# give it math
house_cost(300 + 900, 10 * 200)


print("The fourth way:")
# give it combination of math and variables
house_cost(basic + 100, decoration * 9)


print("The fifth way:")
# give it math between variables
house_cost(basic + decoration, decoration)


print("The sixth way:")
basic = decoration
house_cost(basic, decoration)


print("The seventh way:")
house_cost(100, decoration)


