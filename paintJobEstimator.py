import math
#Function decleration
def get_float_value(prompt):
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

#INPUT
#Declare variables for known values
hourly_labor_cost = 62.25
unit_of_wall_area = 350
hours_labor_per_unit = 6
#prompt the user to enter the amount of wall to paint
#convert into float value
#if error in input ask user to reenter input, input must be greater than 0
wall_area = get_float_value("What is the area of the wall in sq/ft? ")
#prompt user to enter cost of paint per gallon
paint_price = get_float_value("What is the price of paint per gallon? ")

#PROCESS
#Calculate to hours of labor
hours_of_labor = wall_area / unit_of_wall_area * hours_labor_per_unit

#Calculate the cost of labor
cost_of_labor = hours_of_labor * hourly_labor_cost

#Calculate the amount of paint
gallons_of_paint = math.ceil(wall_area / unit_of_wall_area)

#Calculate the cost of the paint
cost_of_paint = gallons_of_paint * paint_price

#Calculate total cost of the job
total_cost = cost_of_labor + cost_of_paint

#OUTPUT
#Print hours of labor, cost of labor, amount of paint, 
print("\nReport\n-------------------")
print(f"Hours of labor: {hours_of_labor:.2f}\nCost of labor: ${cost_of_labor:.2f}\nAmount of paint (gallons): {gallons_of_paint:.2f}")

#cost of paint, total job cost
print(f"Cost of paint: ${cost_of_paint:.2f}\nTotal job cost: $9{total_cost:.2f}")
