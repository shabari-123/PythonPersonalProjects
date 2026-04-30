#Simple program to greet user
def greet():
    name=input("Enter your name: ")
    if name:
        print(f"Hello, {name}! Welcome to the program")
    else:
        print("Hello! you did not enter your name")
    
#call the function
greet()