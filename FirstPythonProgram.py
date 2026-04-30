#Simple program to greet user
def greetName():
    name=input("Enter your name: ")
    #Empty name validation
    if name:
        print(f"Hello, {name}! Welcome to the program")
    else:
        print("Hello! you did not enter your name")
    
#call the function
greetName()