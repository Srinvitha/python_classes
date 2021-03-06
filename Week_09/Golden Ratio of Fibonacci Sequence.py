# Program to display the Fibonacci sequence up to n-th term where n is provided by the user.
# Eg : Fibonacci sequence upto 10 : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
# Observe the Ratio - this is the GOLDEN Ratio.

nterms = int(input("How many terms ??? "))

# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer.")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print(n1,' , ',n1/n2)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

