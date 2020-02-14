#separates all values in the list [1,2,3,4,5,6,7,8,9] in two other lists as odd and even numbers

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_nums = []
even_nums = []

for x in num_list:
    if x % 2 == 0:
        even_nums.append(x)
    else:
        odd_nums.append(x)

print("The odd numbers in the list are:" , odd_nums)
print("The even numbers in the list are:" , even_nums)


