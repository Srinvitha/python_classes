# 2. Program to find the sum of all numbers stored in a list, eg: numbers = [-6, 5, 3, 8, 4, 2, 5, 40].


total = 0
ele = 0

# creating a list
list1 = [-6, 5, 3, 8, 4, 2, 5, 40]

# Iterate each element in list
# and add them in variale total
while (ele < len(list1)):
    total = total + list1[ele]
    ele += 1

# printing total value
print "Sum of all elements in given list: ", total





# creating a list
list1 = [-6, 5, 3, 8, 4, 2, 5, 40]

# using sum() function
total = sum(list1)

# printing total value
print "Sum of all elements in given list: ", total
