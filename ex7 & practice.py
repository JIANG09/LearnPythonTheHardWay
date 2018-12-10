print('Mary has a little lamb.')  # print out a string

# print out a formatted string with a string inside
print("Its fleece was white as {}.".format('snow'))
# print out a string
print("And everything that Mary went.")

# print out '.' for ten times.
print("." * 10)
# from end1 to end12, those are variables; each is bound to a string
end1 = "C"
end2 = 'h'
end3 = 'e'
end4 = 'e'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

# watch end = '' at the end. try removing it to see what happen
# end=' ' means there is a space after the printed string and no next line
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')

# concatenation from end7 to end12, the strings stored in the variables will be concatenated.
print(end7 + end8 + end9 + end10 + end11 + end12)
