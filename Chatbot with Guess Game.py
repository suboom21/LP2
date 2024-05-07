import random

def roll_dice():
    return random.randint(1, 6)

def greet(bot_name, birth_year):
    print(f"Hello, my name is {bot_name}.\nI was created in {birth_year}.")
    
def remind_name():
    name = input("Please remind me of your name: ")
    print(f"What a greate name you have {name}")

def count():
    print("Now I will prove to you that I can coun to any number that you want: ")
    n = int(input())
    for i in range(0, n+1):
        print(i)
def guess_number():
    while True:
        try:
            guess = int(input("Guess the number (1-6): "))
            if 1 <= guess <= 6:
                return guess
            else:
                print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Please enter a valid number.")

def play_game():
    while True:
        print("Ai will roll dice")
        print("You can guess")
        
        target_number = roll_dice()
        user_guess = guess_number()
        
        print(f"\nThe dice rolled: {target_number}")
        if user_guess == target_number:
            print("Congratulations! You guessed it right!")
        else:
            print(f"Sorry, the correct number was {target_number}. Better luck next time!")
        
        play_again = input(" play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
def end():
    print('Congratulations, have a nice day!')
  
    input()
def test():
    print('1.Greet again?')
    print('2.I can count ')
    print('3.End')
    print('4.Game Of number')
   
    print('Completed, have a nice day!')
test()   
x=int(input('Choice?'))
if(x==1):
    greet('Shubhu', '2024')
elif(x==2):
    count()
elif(x==3):
    end()
elif(x==4):
    play_game()


    
    


