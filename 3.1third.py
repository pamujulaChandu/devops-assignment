#getting the list values from the users and some simple mathamatical ops

total=0
exp=[]

num_of_exp=int(input("no.of expensives:\n"))

for i in range(num_of_exp):
    exp.append(int(input(f"expensives of the day {i}:")))
total= sum(exp)
print("total ammount is", total)