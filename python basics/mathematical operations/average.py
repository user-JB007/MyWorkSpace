#using python function

# number = [10,20,30,40]
# avrg= sum(number)/len(number)
# print(f"the total sum is {avrg}")

#without using python function
numbers = [10,20,300,40,50]
total_sum = 0
count = 0

for n in numbers:
    total_sum+=n
    count+=1
avrg = total_sum/count

print(f"the total sum is {avrg}")