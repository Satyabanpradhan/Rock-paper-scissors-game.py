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

user_choice = int(input("what do you chhose ? Type 0 for rock,1 for paper or 2 for scissors : \n"))
print("#Your choice:-")
if (user_choice < 0 or  user_choice > 2 ):
    print("You entered an invalid number, so the computer will choose randomly for you.")
    user_choice = random.randint(0, 2)
    print(game_images[user_choice])

    print("#computer choice :- \n")
    computer_choice = random.randint(0, 2)
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Won !")
    elif user_choice == 1 and computer_choice == 0:
        print("You Won !")
    elif user_choice == 2 and computer_choice == 1:
        print("You Won !")
    elif user_choice == 2 and computer_choice == 0:
        print("You loose !")
    elif user_choice == 0 and computer_choice == 1:
        print("You loose !")
    elif user_choice == 1 and computer_choice == 2:
        print("You loose !")
    elif user_choice == computer_choice:
        print("the match is draw !")
    else:
        print("somthing is wrong")

else:
    print("\n #user choice")
    print(game_images[user_choice])

    print("#computer choice :- \n")
    computer_choice = random.randint(0, 2)
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Won !")
    elif user_choice == 1 and computer_choice == 0:
        print("You Won !")
    elif user_choice == 2 and computer_choice == 1:
        print("You Won !")
    elif user_choice == 2 and computer_choice == 0:
        print("You loose !")
    elif user_choice == 0 and computer_choice == 1:
        print("You loose !")
    elif user_choice == 1 and computer_choice == 2:
        print("You loose !")
    elif user_choice == computer_choice:
        print("the match is draw !")
    else:
        print("somthing is wrong")
