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


---'   ____)____
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
game_images = [rock ,paper,scissors]

user_choice = int(input("what do you chhose ? Type 0 for rock,1 for paper or 2 for scissors : "))
if user_choice >= 0 and user_choice <=2:
    print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("computer choose ")
print(game_images[computer_choice])


if user_choice >= 3 or user_choice < 0:
    print("you typed an invalid number . you lose!")
elif (computer_choice == 0 and user_choice == 2):
    print("you won")
elif (user_choice ==0 and  computer_choice == 2):
    print("you loose !")
elif (computer_choice > user_choice):
    print("you loose !")
elif(user_choice >computer_choice):
    print("you won!")
elif computer_choice == user_choice:
    ("the game is draw")

else:
    print("You typed an invalid number . you lose!")
