# 8. Program to check if a string is palindrome or not (ignoring case and space).

      # Program 1 is by considering case and space while Program 2 is the answer.If you want to see Program 1 work then uncomment it once.
# # function which return reverse of a string
# def reverse(s):
#     return s[::-1]
#
#
# def isPalindrome(s):
#     # Calling reverse function
#     rev = reverse(s)
#
#     # Checking if both string are equal or not
#     if (s == rev):
#         return True
#     return False
#
#
# # Driver code
# c = "mom"
# ans = isPalindrome(c)
# print(c)
#
# if ans == 1:
#     print "Yes,", c , "is a palindrome."
# else:
#     print "No,", c, "is not a palindrome."


from string import punctuation, ascii_lowercase                        # Same for 9th question.

def is_palindrome(string):
    """Return True if string is a palindrome,
    ignoring whitespaces and punctuation.
    """
    new = ""
    for char in string:
        lc = char.lower()
        for x in lc:
            if x in ascii_lowercase:
                new += x

    return new[::-1] == new

string = "Was it a rat I saw?"
print (string)
print is_palindrome(string), ", It is a palindrome."


d = "mada m"                                     # My idea of palindrome finding.:p .:) .
print(d)
r = d[::-1]
print(r)

i = 0
z = len(d)


while i < z:
    if d[i] == r[i]:
        print d[i], "==" ,r[i]
        i = i+1
    else:
        i = i+1

print ("\n (: By now you must have understood if it is palindrome or not ???")

