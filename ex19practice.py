def house_cost(basic, decoration):
    print("The total cost is basic adding decoration, that is, %d" % (basic + decoration))


print("The first way: ")
house_cost(100, 500)


print("The second way:")
basic = 900
decoration = 1000
house_cost(basic, decoration)


print("The third way:")
house_cost(300 + 900, 10 * 200)


print("The fourth way:")
house_cost(basic + 100, decoration * 9)


print("The fifth way:")
house_cost(basic + decoration, decoration)


print("The sixth way:")
basic = decoration
house_cost(basic, decoration)


print("The seventh way:")
house_cost(100, decoration)


