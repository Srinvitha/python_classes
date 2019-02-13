# 4. Add natural numbers upto 77 (1+2+....+77).


n = 77

sum = 0

for num in range(0,n+1,1):
    sum = sum+num
    print (sum)                                                    # only if you want to know the numbers also.
print "SUM of natural numbers upto", n, "is :", sum , "."
