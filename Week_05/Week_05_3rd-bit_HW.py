# Python program to check if the input number is prime or not.

n = int(input("Enter a number: "))
print_statement = "This is a PRIME number."
i=2
while i < n :
    if (n%i)==0 :
        print_statement = "It is not prime... It is Composite. "
        break
    i = i+1

print(print_statement)

# This is an alternate.

