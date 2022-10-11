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
#code below this line 👇
games_images = [rock, paper, scissors]

print("Welcome to game rock, paper, and scissor")
print("----------------------------------------\n")
print(
    "For play the game you have to choose 0 for rock, 1 for paper, and 2 for scissors\n"
)
user_choice = int(input("Let's play, choose number : "))
if user_choice >= 3 or user_choice <= 0:
    print("You input invalid number")
else:
    print(games_images[user_choice])
    computer_choice = random.randint(0, 2)
    print(f"Computer choose : {computer_choice}")
    print(games_images[computer_choice])

    if user_choice == 0 and computer_choice == 1:
        print("Computer win")
    elif computer_choice == 0 and user_choice == 1:
        print("You win")
    elif user_choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice == 0 and user_choice == 2:
        print("computer win")
    elif user_choice == 1 and computer_choice == 2:
        print("Computer win")
    elif computer_choice == 1 and user_choice == 2:
        print("You win")
    elif user_choice == computer_choice:
        print("It's draw")
