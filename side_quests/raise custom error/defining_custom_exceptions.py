#DEFINING THE CUSTOM EXCEPTION

#Define the custom error
class InvalidAgeError(Exception):
    pass

#Try running a piece of validation logic
try:
    age = int(input("Enter your age to vote: "))
    
    if age < 18:
        # Manually throw our custom error if they are too young
        raise InvalidAgeError
    else:
        print("You are eligible to vote!")

#Catch our specific custom error cleanly
except InvalidAgeError:
    print("Access Denied: You must be 18 or older.")