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

def print_main_menu():
    #print the menu
    print("Select option from Menu\n-----------------------")
    print("1. Login")
    print("2. Create User")
    return

def get_user_option():
    while True:
        user_option = input("Would you like to (1) login or (2)create account? ")
        #Ensure the user entered a valid option (1 or 2)
        if user_option != "1" and user_option != "2":
            # -if not, prompt user again
            print("\nERROR: Enter a 1 or 2")
            continue
        else:
            break
    return user_option

def login_user():
# - validate username and password combination in the users.txt file
    #open the users files
    user_file = open("users.txt", "r")
    user_found = False

    while True:
        #If user chose 1, ask for user name and password and
        user_name = input("Please enter your user name: ")
        user_pass = input("Please enter your password: ")

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

        #read the lines from the file
        
def create_user():
    while True:
        user_name = validate_username_or_password("Please enter your username: (4 - 12) characters: ", 4, 12)
        user_pass = validate_username_or_password("Please enter your password: (6 - 16) characters: ", 6, 16)

        try:
            user_file = open("users.txt", "a")
            user_file.write(f"{user_name}, {user_pass}\n")
        except:
            print("Error creating user.\n")
            continue
        else:
            print(f"User {user_name} created")
        finally:
            user_file.close()
        return


def validate_username_or_password(prompt, min_length, max_length):
    while True:
        user_input = input(prompt)
        input_length = len(user_input)

        if (input_length >= min_length and input_length <= max_length):
            break
        else:
            print("ERROR: input length invalid.\n")
    return user_input 

def get_letter_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"

def load_student_scores(number_students):
    student_name, student_score, student_grade = [], [], []
    for x in range (number_students):
        student_name.append(input("What is the name of your student? "))
        student_score.append(validate_number("What is the grade of your student (percent)? "))
        student_grade.append(get_letter_grade(student_score[x]))

    print("\n")
    class_total = 0

    for x in range (number_students):
        print(f"{student_name[x]}: {student_score[x]}%, {student_grade[x]}")
        class_total = class_total + student_score[x]

    class_average = class_total / number_students
    print(f"Class average = {class_average}%")

def main():
    print_main_menu()
    #prompt and get the option the user selected
    user_option = get_user_option()

    if user_option == "1":
        login_user()
    
    #If user chose 2, ask for user name and password and
    elif user_option == "2":
        create_user()

    #Create 3 empty list for student name, scores, letter grades
    number_students = int(validate_number("How many students do you have? "))
    load_student_scores(number_students)

main()
