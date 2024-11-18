#using python function

# number = [10,20,300,40,50]
#
# max_val = max(number)
#
# print(f"the max val is {max_val}")

#without #using python function
numbers = [10,20,300,40,50]
max_val = numbers[0]
for n in numbers:
    if n>max_val:
        max_val=n

print(f"the total sum is {max_val}")