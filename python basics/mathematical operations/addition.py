#using python function
#
# number = [10,20,30,40,50]
#
# total_sum = sum(number)
#
# print(f"the total sum is {total_sum}")

#without #using python function
numbers = [10,20,30,40,50]
total_sum = numbers[0]
for n in numbers:
    total_sum+=n
print(f"the total sum is {total_sum}")