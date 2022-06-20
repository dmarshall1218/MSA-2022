list_of_numbers = [6, 5, 3, 8, 4, 2, 5, 11, 53, 17, 27, 99, 62, 61, 51, 47]

for number in list_of_numbers:
    print(number)

print("\n\n")
number_of_items_in_list = len(list_of_numbers)
for index in range(number_of_items_in_list):
    print(f"Item {index}: {list_of_numbers[index]}")