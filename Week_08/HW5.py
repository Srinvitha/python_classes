# Write a python script which generates a random number between 0 and 13.
# Check if the random number is prime or not by passing it to a function which checks for prime number and returns true or false.



import random

r = (random.randint(1,27))
print r

# Python program to check if the input number is prime or not.

print_statement = "This is a PRIME number."
i=2
while i < r :
    if (r%i)==0 :
        print_statement = "It is not prime... It is Composite. "
        break
    i = i+1

print(print_statement)
