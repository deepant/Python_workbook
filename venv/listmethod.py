numbers = [5 , 2 , 1, 7, 4]
numbers.append(20)
print(numbers)
numbers.insert(2, 50)
numbers.insert(4, 50)
print(numbers)
numbers.remove(5)
print(numbers)

print(numbers)
numbers.pop()
print(numbers)
print(50 in numbers)
print(numbers.count(50))
print(numbers.sort())
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
numbers2.insert(4, 60)
print(numbers)
print(numbers2)


n1 = [2 ,2 , 2, 5, 6, 6, 5, 7 ,  3, 1]
unique = []
for n in n1:
    if n not in unique:
        unique.append(n)
print(unique)