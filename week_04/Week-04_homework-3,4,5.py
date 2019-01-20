# Find whether the given 2 digit number AB contain the digit d.
# Given a 2 digit number AB is it greater than A power B.
# You are given 3 numbers a, b and x. You need to output the multiple of x which is closest to a power b.




                                                                                                                    # 3
AB = input(" Enter any (positive) 2-digit number of your choice => \n")
print("\n")

s = AB/10
print (int(s))

r = AB%10
print (int(r))

d = 8
print("\n")

if s == d :
    print ("The tens digit equals 'd'.")
else:
    print ("The tens digit is not equal to 'd'.")

if r == d :
    print ("The ones digit equals 'd'.")
else:
    print ("The ones digit is not equal to 'd'.")

print("\n")
print("\n")
print("\n")
print("\n")

                                                                                                                    # 4
ab = input(" Enter any (positive) 2-digit number of your choice => \n")
print("\n")

p = ab/10
print (int(p))

q = ab%10
print (int(q))

if p**q>ab:
    print ("p^q is greater than ab...")
if p**q<ab:
    print ("ab is greater than p^q...")


print("\n")
print("\n")
print("\n")
print("\n")

                                                                                                                    # 5
a = input(" Enter a number 'a' of your choice => \n")
b = input(" Enter a number 'b' of your choice => \n")
x = input(" Enter a number 'x' of your choice => \n")

f = a**b
print (f)


w = f/x
j=(int(w))
print (j)

y = x*j
print (y)

print("\n")

print ("My Week_04 homework thus ENDS... :) ")


