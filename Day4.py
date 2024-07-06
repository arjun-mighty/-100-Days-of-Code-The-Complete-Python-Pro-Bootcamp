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
game_images = [rock,paper,scissors]
user_choice=int(input("What do you choose? Type 0 for rock,1 for paper,2 for scissors\n"))
if user_choice>=3 or user_choice<0:
      print("You entered invalid number")
print(game_images[user_choice])

computer_choice=random.randint(0,2)
print("Computer choose:")
print(game_images[computer_choice])


if user_choice==0 and computer_choice==2:
    print("You won")
elif user_choice==2 and computer_choice==0:
    print("You lose")
elif computer_choice>user_choice:
    print("You lost")
elif user_choice>computer_choice:
    print("you win")
elif user_choice==computer_choice:
    print("Its a draw")

      