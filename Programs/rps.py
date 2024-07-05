import random
def computer_choice():
    return random.choice(['rock', 'paper', 'scissor'])

def user_choice():
    x = input("Make your choice: ")
    if x not in ['rock', 'paper', 'scissor']:
        print("Invalid choice")
        x = input("Make your choice: ")
    return x

def winner(user, computer):
    if user == computer:
        return "Its a tie!"
    elif ((user == 'rock' and computer == 'scissor') or
          (user == 'paper' and computer == 'rock') or
          (user == 'scissor' and computer == 'paper')):
        return "Winner: User!"
    else:
        return "Winner: Computer!"

computer = computer_choice()
user = user_choice()
result = winner(user, computer)
print("Your choice: ", user)
print("Computer choice: ", computer)
print(result)