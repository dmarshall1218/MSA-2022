import math
#This is the loop that checks for valid numbers and prompts the user on crashes and errors
def check_values(prompt):
    loop = True
    while(loop):
        try:
            user_input = float(input(prompt))
            if(user_input <= 0):
                print("ERROR: value must be above 0.\n")
                continue
        except:
            print("ERROR: input must be a positive number.\n")
        else:
            loop = False
    return user_input

loop2 = True
while(loop2):
    #Determine variables
    height = check_values("\nWhat is the height of the cylinder? ")
    radius = check_values("\nWhat is the radius of the cylinder? ")

    #Math
    volume = height * radius**2 * math.pi
    print(f"\nThe volume of the cylinder is: {volume}")
    run_again = input("Would you like to perform another calculation? (Please input \"y\" for yes and \"n\" for no) ")
    if (run_again == "n"):
        loop2 = False