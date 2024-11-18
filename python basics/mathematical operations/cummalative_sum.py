import itertools

data = [1, 2, 3, 4, 5]
cumulative_sum = list(itertools.accumulate(data))
print(cumulative_sum)  # Output: [1, 3, 6, 10, 15]


#for loop
data = [1, 2, 3, 4, 5]
cumulative_sum = []
current_sum = 0

for num in data:
    current_sum += num
    cumulative_sum.append(current_sum)

print(cumulative_sum)  # Output: [1, 3, 6, 10, 15]
