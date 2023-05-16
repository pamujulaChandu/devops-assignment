#rock paper scissor
# import and using RANDOM lib and playing the game with type of STRING values....by (random.choice([]))


import random

computer_choice= random.choice(["rock", "paper", "scissor"])
user_choice=input("select one - rock, paper or scissor\n")

if computer_choice==user_choice:
    print("tie")
elif (user_choice== "rock"and computer_choice=="scissor") or (user_choice== "paper"and computer_choice=="rock") or (user_choice== "scissor"and computer_choice=="paper"):
    print(f"user WINS as computer choose {computer_choice}")
else:
    print(f"computer WINS as computer choose {computer_choice}")
