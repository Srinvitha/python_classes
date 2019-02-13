# 7. Iterate through string - abcdefghijklmnopqrstuvwxyz - and print the string without vowels in it Vowels : a,e,i,o,u.

vowels=['a','e','i','o','u']
y= "abcdefghijklmnopqrstuvwxyz"
y = y.lower()
for v in vowels:
    y = y.replace(v, "  ")
    print(y)
print("No VOWELS !!! (:) ")
