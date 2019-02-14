# 6. Create a string, access its characters and print them in separate lines.


str = str("Srinvitha")
print (str)

l = len(str)
print (l)

while l > 0:
    l = l-1
    print (str[l])

print ("\n")                                                          # Method 2

t = "Python"
print(t)

m = len(t)
print(m)
x = -1
while x < m:
    x = x + 1
    if x >= m:
        break
    else:
        print (t[x])

print ("\n")                                                          # Method 3


word = 'lead'
print(word)
for char in word:
    print(char)
