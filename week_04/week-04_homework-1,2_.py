# 1. Input a number n, find whether divided by 2.
# 2. Input a number n, find whether divided by 6.

n = (int(input(" Enter any number of your choice => \n")))
print("\n")

if n % 2 == 0:
    print ("This number is divisible by 2.")

else:
    print ("This number is not divisible by 2 .")

if n % 6 == 0:
    print ("And this number is divisible by 6.")

else:
    print ("This number is not divisible by 6 .")


