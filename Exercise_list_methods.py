#Write a program to remove the duplicates in a list
numbers = [5,2,1,5,4,7,7, 10, 11, 13]
uniques =[]
numbers.sort()
print(numbers)

for value in numbers:
    if value not in uniques:
        uniques.append(value)
print(uniques)



