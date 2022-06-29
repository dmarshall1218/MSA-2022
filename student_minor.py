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
            print("YaY! Good input")
            break
    return user_option

def login_user(u_name, u_pass):
# - validate username and password combination in the users.txt file
    #open the users files
    user_file = open("users.txt", "r")
    user_found = False

    #read the lines from the file
    for line in user_file:
        credentials = line.split(", ")
        #compare username and password for a match
        if u_name == credentials[0] and u_pass == credentials[1].rstrip():
            user_found = True
            break
    return user_found

def main():
    print_main_menu()
    #prompt and get the option the user selected
    user_option = get_user_option()

    if user_option == "1":
        while True:
            #If user chose 1, ask for user name and password and
            user_name = input("Please enter your user name: ")
            user_pass = input("Please enter your password: ")

            user_logged_in = login_user(user_name, user_pass)

            if user_logged_in:
                # - if valid then move on to prompt for student data
                print(f"User {user_name} successfully logged in!\n")
                break
            else:
                # - if not valid combination reprompt the user. 
                print(f"User {user_name} not found!\n")
    
    #If user chose 2, ask for user name and password and
    elif user_option == "2":
        while True:
            #If user chose 2, ask for user name and password and
            user_name = input("Please enter your user name (4 - 12 characters): ")
            user_pass = input("Please enter your password: (6 - 16) characters: ")

            #get username and password length
            user_name_length = len(user_name)
            password_length = len(user_pass)
            
            # - validate username and password length. If valid, write to users.txt file
            # 4 <= user_mame_length >= 12
            if (user_name_length >= 4 and user_name_length <= 12) and (password_length >= 6 and password_length <= 16):
                #write user and pass to the file
                user_file = open("users.txt", "a")
                user_file.write(f"{user_name}, {user_pass}\n")
                user_file.close()
                break
            else:
                print("ERROR: Incorrect username or password length.\n")

    print("Ask user for student data")
    #Create 3 empty list for student name, scores, letter grades
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

    class_total = 0

    for x in range (number_students):
        print(f"{student_name[x]}: {student_score[x]}%, {student_grade[x]}")
        class_total = class_total + student_score[x]

    class_average = class_total / number_students
    print(f"Class average = {class_average}%")

main()
