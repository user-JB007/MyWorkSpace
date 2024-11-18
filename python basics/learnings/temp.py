def celsius_to_fahrenheit_kelvin(temp_c):
    cel_far = (9 / 5) * temp_c + 32
    cel_kel = temp_c + 273.15
    return cel_far, cel_kel

def fahrenheit_to_celsius_kelvin(temp_f):
    far_cel = 5 / 9 * (temp_f - 32)
    far_kel = far_cel + 273.15
    return far_cel, far_kel

def kelvin_to_celsius_fahrenheit(temp_k):
    kel_cel = temp_k - 273.15
    kel_far = 9 / 5 * kel_cel + 32
    return kel_cel, kel_far

def main():
    print("Let's calculate the temperature units!\nWhich temperature unit value do you like to convert?")
    option = {1: "celsius", 2: "fahrenheit", 3: "kelvin"}

    while True:
        try:
            user_choice = int(input("Enter temperature unit code - 1 for Celsius, 2 for Fahrenheit, 3 for Kelvin: "))
            if user_choice in option:
                selected_unit = option[user_choice]
                print(f"Selected temperature unit is {selected_unit}")
            else:
                print("Bugger, you've entered an invalid temperature unit.\nEnter a valid temperature unit from the option: ")
                continue
        except ValueError:
            print("Please enter a valid integer for the temperature code: ")
            continue

        if selected_unit == "celsius":
            while True:
                try:
                    temp_c = float(input("Mention the temperature in Celsius: "))
                    break
                except ValueError:
                    print("Enter the temperature in integer or float: ")
            cel_far, cel_kel = celsius_to_fahrenheit_kelvin(temp_c)
            print(f"The temperature in Fahrenheit is {cel_far} and Kelvin is {cel_kel}.")

        elif selected_unit == "fahrenheit":
            while True:
                try:
                    temp_f = float(input("Mention the temperature in Fahrenheit: "))
                    break
                except ValueError:
                    print("Enter the temperature in integer or float: ")
            far_cel, far_kel = fahrenheit_to_celsius_kelvin(temp_f)
            print(f"The temperature in Celsius is {far_cel} and Kelvin is {far_kel}.")

        else:
            while True:
                try:
                    temp_k = float(input("Mention the temperature in Kelvin: "))
                    break
                except ValueError:
                    print("Enter the temperature in integer or float: ")
            kel_cel, kel_far = kelvin_to_celsius_fahrenheit(temp_k)
            print(f"The temperature in Celsius is {kel_cel} and Fahrenheit is {kel_far}.")

        ans = input("Do you like to convert another temperature unit? [Y/N]: ").lower()

        while ans not in ['y', 'n']:
            ans = input("User option is invalid.\nEnter a valid option: ")

        if ans == 'n':
            break

    print("Thanks for using the temperature unit converter.")

if __name__ == "__main__":
    main()
