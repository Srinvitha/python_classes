
num = int(input("Enter a number ... \n"))

# Changed num variable to string,
# and calculated the length (number of digits)
order = len(str(num))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")




# Python Program For Armstrong Number using While Loop

Number = int(input("\nPlease Enter the Number to Check for Armstrong: "))

# Initializing Sum and Number of Digits
Sum = 0
Times = 0

# Calculating Number of individual digits
Temp = Number
while Temp > 0:
   Times = Times + 1
   Temp = Temp // 10

# Finding Armstrong Number
Temp = Number
while Temp > 0:
   Reminder = Temp % 10
   Sum = Sum + (Reminder ** Times)
   Temp //= 10
if Number == Sum:
   print("\n %d is Armstrong Number.\n" % Number)
else:
   print("\n %d is Not a Armstrong Number.\n" % Number)

num = int(input("enter a number: "))

length = len(str(num))
sum = 0
temp = num

while (temp != 0):
   sum = sum + ((temp % 10) ** length)
   temp = temp // 10

if sum == num:
   print("armstrong number")
else:
   print("not armstrong number")


