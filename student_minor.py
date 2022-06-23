#Print the menu
print("Select option from Menu")
print("-----------------------")
print("Login: 1")
print("Create a user: 2")

#Get the option the user selected
while True:
    option = input("Would you like to (1) login or (2) create an account? ")
    #Ensure the user entered a valid option
        #   if not, prompt user again
    if option != "1" and option != "2":
        print("ERROR: Enter a 1 or 2.")
        continue
    else:
        print("YAY GOOD INPUT")
        break
        

#If user chose 1, ask for username and password
#   check username and password combination in the users.txt file
#   if not valid combination prompt user
#   if valid then move on to prompt for student data
#If user chose 2, ask for username and password
#   validate username and password length
#   if valid, write to users.txt file
#   and move on to the student data
#   if not valid then reprompt the user

#Ask user how many students to enter data for
#prompt user to enter student name and percentage score
#store data somewhere
#convert the number score to a letter grade

#print student data(name, score, grade)
#calculate and print the class average