list_of_nums = list(map(int, input('Enter integers separated by spaces: ').split()))
minimum = None
maximum = None

for i in range(len(list_of_nums)):
    if minimum is None or list_of_nums[i] < minimum:
        minimum = list_of_nums[i]   

    if maximum is None or list_of_nums[i] > maximum:
        maximum = list_of_nums[i]

print(maximum - minimum)
