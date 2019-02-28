# Count the number of prime numbers less than 2000 and time it.


import time as t

start = t.clock()

primes = [2,3,5,7]

for num in xrange(2,200000):
    if all(num%x != 0 for x in primes):
        primes.append(num)

print primes
print (t.clock() - start, "Seconds.")
print (len(primes), "Primes")
print (sum(primes), "is the sum of all these prime numbers.")

# # Count the number of prime numbers less than 2000 and time it.
#
# from time import clock
# from math import sqrt
#
# count = 0
# def count_primes(n):
#     '''
#     Generates all the primes from 2 to n-1'
#     n-1 is the largest potential prime considered.
#     '''
#
#     start = clock()  # Record Start time.
#
#     count = 0
#     for val in range(2, n):
#         result = True  # Provisionally, n is prime.
#         root = int(sqrt(val) + 1)
#
#         trial_factor = 2
#         while result and trial_factor <= root:
#             result = (val % trial_factor != 0)
#             trial_factor += 1
#         if result:
#             count += 1
#
#
# stop = clock()  # Stop the Clock.
# print("Count = ", count, "Elapsed Time:", stop - start, "seconds")
#
#
# def lol(n):
#     start = clock()
#
#     nonprimes = n * [False]
#
#     count = 0
#
#     nonprimes[0] = nonprimes[1] = True
#
#     for i in range(2, n):
#         if not nonprimes[i]:
#             count += 1
#     for j in range(2 * i, n, i):
#         nonprimes[j] = True
#
#     stop = clock()
#     print("Count = ", count, "Elapsed Time:", stop - start, "seconds")
#
#
# def main():
#     count_primes(2000)
#     lol(2000)
#
#
# main()

