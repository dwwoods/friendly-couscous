#learning about .methods for list
numbers = [5,2,1,5,4,7]

numbers.append(20) #methods
print(numbers)

numbers.insert(0,10)
print(numbers)

numbers.remove(5)
print(numbers)

numbers.pop()
print(numbers)
print(numbers.count(5))
print(numbers.index(4))
print(50 in numbers) # boolean result
print(10 in numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()

numbers.clear()
print(numbers)
print(numbers2)