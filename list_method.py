numbers = [5, 2, 5, 5, 6, 1, 14]

#methods

#add an item
numbers.append(20)
print(numbers)

#insert an item in a place (index, item to add)
numbers.insert(0, 34)
print(numbers)

#removing an item
numbers.remove(2)
print(numbers)

#remove all items in list
#numbers.clear()

#remove last item
numbers.pop()
print(numbers)

#show index of first occurance of an item
print(numbers.index(6))
#can also use in to return a boolean(safer)
print(1 in numbers)

#how many times an item occurs in a list
print(numbers.count(5))

#sort list
numbers.sort()
print(numbers)

#sort list in reverse
numbers.reverse()
print(numbers)

#copy list
numbers2 = numbers.copy()
print(numbers, numbers2)
numbers.append(10)

print(numbers)
print(numbers2)

'''Write a program that removes duplicates'''
numb = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numb:
    if number not in uniques:
        uniques.append(number)
    else:
        pass
print(uniques)