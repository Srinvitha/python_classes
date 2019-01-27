
fruits = ["Mango", "Strawberry", "Pineapple", "Custard-apple", "Apple", "Banana"]

print(fruits)

num_list = [1, 2, 3, 4, 5, 6]
fruits.append(num_list)                                                           # Append
print(fruits)

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])
print(fruits[5])
print(fruits[6])

print("\n")

fruits.extend(num_list)                                                           #Extend
print (fruits)

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])
print(fruits[5])
print(fruits[6])

print("\n")

list_itself = [1, 2, 3, 4, 5, 6, 7, 8]
print (list_itself)
list_itself.extend(list_itself)
print (list_itself)
list_itself.insert(4, "10")                                                   #Insert
print(list_itself)

