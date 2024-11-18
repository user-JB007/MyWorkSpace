# y=int(input("Provide the number: "))
# # if y % 8 == 0:
# #     print ("Not divisible by 8!")
# if y % 3 == 0 and y % 2 == 0 and y % 8 != 0:
#     print ("Yes")
# else:
#     print("No")

year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")