# Step 1: Define variables
# # rent_amount = 1000
# number_of_months = 12
# additional_fees = 100
while True:
    print("Let's calculate the rent amount.")
# Step 2: Get user input
    rent_amount = float(input("Enter the rent amount: "))
    number_of_months = int(input("Enter the number of months: "))
    additional_fees = int(input("Enter the additional fees: "))

# Step 3: Calculate total rent
    total_rent = rent_amount * number_of_months
    tot_adtnl_fee=additional_fees*number_of_months

# Step 4: Add additional fees
    total_rent += tot_adtnl_fee
 
# Step 5: Display the result
    print("Total rent: ", total_rent)

    print("Do you want to calculate for other amount? [Y/N] ")
    ans=input().lower()
    
    while ans not in ['n','y']:
        ans=input("User option is invalid.\n"
                      + "Enter a valid option: ")
    if ans=='n':
        break

print("Thanks for using our rent calculator.")