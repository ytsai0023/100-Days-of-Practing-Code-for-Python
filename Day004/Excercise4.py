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

gesture =  [rock,paper,scissors]
choice = int(input("(1)rock (2)paper (3)scissors"))
my_choice_gesture = gesture[choice-1]
computer_choice = random.randint(1,3)
computer_choice_gesture = gesture[computer_choice-1]

winner = ""
print(f"You:{my_choice_gesture}")
print(f"Computer:{computer_choice_gesture}")

if choice == computer_choice:
  print("You are fair!")
else:
  if choice == 1 and computer_choice == 2:
    winner = "Computer"
  elif choice == 1 and computer_choice == 3:
    winner = "You"
  if choice == 2 and computer_choice == 3:
    winner = "Computer"
  elif choice == 2 and computer_choice == 1:
    winner = "You"
  if choice == 3 and computer_choice == 1:
    winner = "Computer"
  elif choice == 3 and computer_choice == 2:
    winner = "You"
  print(f"{winner} won this game!")       


