# 1. Input a sentence from terminal, convert it into lower, upper, capitalize.


# s = str(input(" Input a sentence with only alphabets. "))

s = "Hello!!!"

print(s.lower())
print(s.upper())
print(s.capitalize())

def string_to_uppercase(s):
    y = s.upper()
    return y


# fruits = str(input(" What is you favourite fruit ??? "))

fruits = "LitchI"

for f in fruits:
    print(string_to_uppercase(f))
