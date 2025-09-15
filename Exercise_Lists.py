numbers = [2, 1, 5, 4, 3, 6, 8, 10, 9, 7]
#sorted_numbers = sorted(numbers)
#print(sorted_numbers)
#max = sorted_numbers[-1]
#print(max)
max_value = numbers[0]
for number in numbers:
    if number > max_value:
        max_value = number
        print(max_value)
print (max_value)
