# Conditional Statements in Python

# if statement
x = 10
if x > 5:
    print("x is greater than 5")    
else:
    print("x is not greater than 5")
    
# if-elif-else statement
y = 15
if y < 10:
    print("y is less than 10")
elif y > 20:
    print("y is greater than 20")
else:
    print("y is between 10 and 20")
    
# nested if statement
z = 25
if z < 10:
    print("z is less than 10")
else:
    if z > 20:
        print("z is greater than 20")
    else:
        print("z is between 10 and 20")
        
# ternary operator
a = 30
b = 40
print("a is greater than b") if a > b else print("b is greater than a")


# Match-case statement
command = "exit"
match command:
    case "start":
        print("Starting the program")
    case "stop" | "exit":
        print("Stopping the program")
    case _:
        print("Unknown command")
        
        

# Example of a simple login system using nested if statements

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
        print("Access granted")
    else:
        print("Incorrect password")
else:
    print("Username not found")