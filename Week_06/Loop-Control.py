# Loop Control Statements => 1. Break, 2. Pass .
print ("\n")

numbers_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]                    #Break

for n in numbers_list:
    print(n)
    if n == "5":
        break

print ("\n")

general_list = ["1", 24, "Happy", False, ":)", 42.682, "Girl", True]      #Pass

for gen in general_list:
    print(gen)
    if gen == 24:
        pass

