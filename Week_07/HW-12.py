# 12. Concatenate a string by itself 30 times using loop.


print("ha" * 30)                                              # Without using loop.

s = "Ha!"
l = []
n = 0
while n < 30:
    n = n+1
    s*n
    l.append(s)

    if n == 30:
        print (l)
        print (len(l))

