# prompt for user input

user_input_name = input("What is your name?")
print( f"\nYour name is { user_input_name }!" )

added_numbers = 0
user_input_numbers = input(f"\nType a number (or leave blank to exit)")


while user_input_numbers != "":
    user_input_numbers = input(f"\nType a number (or leave blank to exit)")
    if user_input_numbers != "":
        added_numbers += int(user_input_numbers)

print(f"\n{added_numbers}")