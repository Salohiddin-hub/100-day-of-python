# import random
#! random_body=random.randint(1,3)
# if random_body == 1:
#     print("Heads")
# elif random_body == 2:
#     print("Tails")
#! Option 1
# friends=["Alice", "Bob", "Charlie", "David", "Emanuel"]
# print(random.choice(friends))
#! # Option 2
# random_friends=random.randint(0,4)
# print(friends[random_friends])

#! fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen[1][1])

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game=[rock, paper,scissors]
human_choice=int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors\n"))
computer_choice=random.randint(0,2)
print(f"Your choice: {game[human_choice]}")
print(f"My choice: {game[computer_choice]}")
if human_choice == computer_choice:
    print("Draw!")
elif (human_choice == 0 and computer_choice == 2) or \
     (human_choice == 1 and computer_choice == 0 ) or \
     (human_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose and I won!")
