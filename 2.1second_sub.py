#importing random lib and using with some rolling die example where input is integer values...
# by using (randint(range))...


import random

roll = random.randint(1,6)

user = int(input("enter any value btw 1 to 6 :\n"))

if(user==roll):
    print("both are same and rolled the number: "+str(roll))
else:
    print("wrong guess as rolled no.: "+str(roll)) 