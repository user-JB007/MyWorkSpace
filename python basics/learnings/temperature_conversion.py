print("Let's calculate the temperature units!\nWhich temperature unit value do you like to convert?")
option = ["celsius", "fahrenheit", "kelvin"]

while True:

    user_choice = input("Enter temperature unit - Celsius, Fahrenheit, Kelvin: ").lower()
    print(f"Selected temperature unit is {user_choice}")

    while user_choice not in option:
        user_choice = input(
            "Bugger, you've entered an invalid temperature unit. \nEnter a valid temperature unit from the option: ").lower()

    if user_choice == "celsius":
        while True:
            try:
                temp_c = float(input("Mention the temperature in Celsius: "))
                break
            except ValueError:
                print("Enter the temperature in integer or float: ")
        # Celsius to Fahrenheit
        cel_far = (9 / 5) * temp_c + 32
        # Celsius to kelvin
        cel_kel = temp_c + 273.15
        print(f"The Celsius in Fahrenheit is {cel_far} and Kelvin is {cel_kel}.")

    elif user_choice=="fahrenheit":
        while True:
            try:
                temp_f = float(input("Mention the temperature in Fahrenheit: "))
                break
            except ValueError:
                print("Enter the temperature in integer or float: ")
        # Fahrenheit to Celsius
        far_cel = 5/9 * (temp_f - 32)
        # Fahrenheit to kelvin
        far_kel = far_cel + 273.15
        print(f"The Fahrenheit in Celsius is {far_cel} and Kelvin is {far_kel}.")

    else:
        while True:
            try:
                temp_k = float(input("Mention the temperature in Kelvin: "))
                break
            except ValueError:
                print("Enter the temperature in integer or float: ")
        # Fahrenheit to Celsius
        kel_cel = temp_k - 273.15
        # Fahrenheit to kelvin
        kel_far = 9/5 * kel_cel + 32
        print(f"The Kelvin in Celsius is {kel_cel} and Fahrenheit is {kel_far}.")

    ans = input("Do you like to convert other temperature units? [Y/N]: ").lower()

    while ans not in ['y','n']:
        ans = input("User option is an invalid.\nEnter a valid option: ")

    if ans=='n':
        break

print("Thanks for using temperature unit converter.")