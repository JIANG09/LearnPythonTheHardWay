name = "Zed A. Shaw"
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = "Brown"

print('Let\'s talk about %r.' % name)
print("He's %r inches tall." % height)
print("He's %r pounds heavy." % weight)
print("Actually that's not too heavy.")
print("He's got %r eyes and %r hair." % (eyes, hair))
print("His teeth are usually %r depending on coffee." % teeth)

# this line is tricky, try to get it exactly right.
print("If I add %r, %r, and %r I get %r." % (age, height, weight, age + height + weight))

# %s: 格式化字符  %d:格式化整数  %f:格式化浮点数字，可指定小数点后的精度  
# %e:用科学计数法格式化浮点数 %g:%f和%e的简写 %r: 不管什么都能打印出来
