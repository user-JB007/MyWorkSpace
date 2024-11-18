
from lib.utils import cel_to_far_kel, far_to_cel_kel, kel_to_cel_far
def main():

    print("Let's calculate the temperature units!\nWhich temperature unit value do you like to convert?")
    option = {1:"celsius", 2:"fahrenheit", 3:"kelvin"}

    while True:
        try:
            user_choice = int(input("Enter temperature unit code- 1 for Celsius, 2 for Fahrenheit, 3 for Kelvin: "))
            if user_choice in option:
                selected_unit=option[user_choice]
                print(f"Selected temperature unit is {user_choice}")
            else:
                print(f"Bugger, you've entered an invalid temperature unit {user_choice}. Enter a valid temperature unit from the option: ")
                continue
        except ValueError:
            print("Please enter a valid integer for the temperature code: ")
            continue

        if selected_unit == "celsius":
            while True:
                try:
                    temp_c = float(input("Mention the temperature in Celsius: "))
                    print(f"Mentioned temperature is {temp_c}")
                    break
                except ValueError:
                    print("Enter the temperature in integer or float: ")
            cel_far, cel_kel = cel_to_far_kel(temp_c)
            print(f"The Celsius in Fahrenheit is {cel_far} and Kelvin is {cel_kel}.")
            input("press enter")

        elif selected_unit=="fahrenheit":
            while True:
                try:
                    temp_f = float(input("Mention the temperature in Fahrenheit: "))
                    break
                except ValueError:
                    print("Enter the temperature in integer or float: ")
            far_cel, far_kel = far_to_cel_kel(temp_f)
            print(f"The Fahrenheit in Celsius is {far_cel} and Kelvin is {far_kel}.")

        else:   #selected_unit=3 is kelvin
            while True:
                try:
                    temp_k = float(input("Mention the temperature in Kelvin: "))
                    break
                except ValueError:
                    print("Enter the temperature in integer or float: ")
            kel_cel, kel_far = kel_to_cel_far(temp_k)
            print(f"The Kelvin in Celsius is {kel_cel} and Fahrenheit is {kel_far}.")

        ans = input("Do you like to convert other temperature units? [Y/N]: ").lower()

        while ans not in ['y','n']:
            ans = input("User option is an invalid.\nEnter a valid option: ")

        if ans=='n':
            break

    print("Thanks for using temperature unit converter.")

if __name__=="__main__":
    main()