#print the menu
from ast import While

def validate_number(prompt):
    run_again = True
    while(run_again):
        try:
            user_input = float(input(prompt))
            if(user_input <= 0):
                print("ERROR: Value must be a positive number.\n")
                continue
        except:
            print("ERROR: Input must be a number.\n")
        else:
            run_again = False

    return user_input

print("Select option from Menu\n-----------------------")
print("1. Login")
print("2. Create User")

#prompt and get the option the user selected
while True:
    user_option = input("Would you like to (1) login or (2)create account? ")
    #Ensure the user entered a valid option (1 or 2)
    if user_option != "1" and user_option != "2":
        # -if not, prompt user again
        print("\nERROR: Enter a 1 or 2")
        continue
    else:
        break     


if user_option == "1":
    while True:
        #If user chose 1, ask for user name and password and
        user_name = input("Please enter your user name: ")
        user_pass = input("Please enter your password: ")
        # - validate username and password combination in the users.txt file
        #open the users files
        user_file = open("users.txt", "r")
        user_found = False

        #read the lines from the file
        for line in user_file:
            credentials = line.split(", ")
             #compare username and password for a match
            if user_name == credentials[0] and user_pass == credentials[1].rstrip():
                user_found = True
                break

        if user_found:
            # - if valid then move on to prompt for student data
            print(f"User {user_name} successfully logged in!\n")
            break
        else:
            # - if not valid combination reprompt the user. 
            print(f"User {user_name} not found!\n")
        
       
        
        

#If user chose 2, ask for user name and password and
elif user_option == "2":
    # - validate username and password length. If valid, write to users.txt file
    while True:
        user_name = input("Please enter your username (4-12 characters): ")
        user_name_length = len(user_name)
        if user_name_length >= 4 and user_name_length <= 12:
            print("Accepted")
            break
        else:
            print("Please enter a username between 4 and 12 characters")
    while True:
        user_pass = input("Please enter your password (6-16 characters): ")
        user_pass_length = len(user_pass)
    
        if user_pass_length >= 6 and user_pass_length <= 16:
            print("Accepted")
            user_file = open("users.txt", "a")
            user_file.write(f"{user_name}, {user_pass}\n")
            user_file.close
            break
        else:
            print("Please enter a password between 6 and 16 characters")


# - and move on
#If not valid re prompt user
#Create 3 empty lists for the student's data
number_students = int(validate_number("How many students do you have?"))
student_name = []
student_score = []
student_grade = []
for x in range (number_students):
    student_name.append(input("What is the name of your student? "))
    student_score.append(validate_number("What is the grade of your student (percent)? "))

print("\n")

for grade in student_score:
    if grade >= 90:
        student_grade.append("A")
    elif grade >= 80:
        student_grade.append("B")
    elif grade >= 70:
        student_grade.append("C")
    elif grade >= 60:
        student_grade.append("D")
    else:
        student_grade.append("F")

for x in range (number_students):
    print(f"{student_name[x]}: {student_score[x]}%, {student_grade[x]}")
#Ask user how many students to enter data for
#prompt user to enter student name and number score
#store data somewhere
#convert the number score to a letter grade 

#Print student data(name, score, grade)
#Calculate and print class average
