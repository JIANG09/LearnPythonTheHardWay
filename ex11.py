print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()
print("So, you're %r old, %r tall and %r heavy." %
      (age, height, weight))

print("What are you doing right now?", end=' ')
doing = input()
print("Why are you doing it?", end=' ')
why = input()
print("How many days have you been doing it? ", end= ' ')
long = int(input())

print("""So, \n\tYou are %s.
             \n\t\t%s
             \n\t\t\tYou have been doing it for %d days. 
             \n\t\t\t\tYour wish will come true!Just keep doing!"""
      % (doing, why, long))

