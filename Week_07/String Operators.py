a = "Hello "
b = ',Python '

# 1. Concatenation - Adds values on either side of the operator '+' .
print (a+b)
# 1. HW
print (a+b+a)

# 2. Slice - Gives the character from the given index.
# 3. Range Slice - Gives the character from the given range.
# 4. Repitition '*'
# 4. HW
print (a*20)

# 5. Membership
# in

if "x" in a:
    print("x is present.")

if "y" in b:
    print("y is present.")



fruits = ["Mango", "Litchi", "Strawberry", "Pineapple", "Custard-apple", "Apple", "Banana"]

x = str(input("What is your favourite fruit ??"))
if x in fruits:
    print('Fruit available.')
else:
    print('Fruit not available.')

general_list = ["1", 24, "Happy", False, ":)", 42.682, "Girl", True]

if "Sadness" not in general_list:
    print('Sadness does not exist here.')
else:
    print('Sadness exists here.')

# 5. Membership
# b. not in

