# Game of Rock Paper Scissors
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
image = [rock,paper,scissors]
print("Choose '0' for Rock '1' for Paper '2' for scissors")
player_choice = int(input("Rock, Paper or Scissors? - "))

computer_choice = random.randint(0,2)
if 0 <= player_choice <= 2:   
    print(f"You chose: \n {image[player_choice]}")
    print(f"Computer Chose: \n {image[computer_choice]}")
    if player_choice > 2 or player_choice < 0:
        print("You typed an invalid number, You lose!")
    elif player_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and player_choice == 2:
        print("You Lose!")
    elif player_choice > computer_choice:
        print("You Win!")
    elif computer_choice > player_choice:
        print("You Lose!")
    elif computer_choice == player_choice:
        print("It's a Draw")
else:
    print("You typed an invalid number")