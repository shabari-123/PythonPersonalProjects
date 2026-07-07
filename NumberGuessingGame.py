#Number Guessing Game
import random

def numGuessingGame():
    print("Welcome to the number guessing game")
    try:
        low=int(input("Enter start range"))
        high=int(input("Enter end range"))
        if low>=high:
            print("Invalid range! Start range cannot be greater than end range")
    except ValueError:
        print("Invalid! Enter only number")
        return
    
    print(f"I am guessing the number between {low} and {high} ")
    secretNum=random.randint(low,high)
    #print(secretNum)
    gc=0
    attempts=5
    
    while gc<attempts:
            try:
                guess=int(input("Enter the guess"))
                gc+=1
                if guess<low or guess>high:
                    print(f"Invalid range! please select the number between the {low} and {high}")
                elif guess<secretNum:
                    print("Too low, Try again!")
                elif guess>secretNum:
                    print("Too high, Try again")
                elif guess==secretNum:
                    print(f"Congrats! you guessed correct number in {gc} attempts")
                    break
            except ValueError:
                print("Enter the only number")
    else:
            print(f"Sorry! You have crossed the {attempts}attempts. Better luck next time")
            
numGuessingGame()                                                                                                                    
