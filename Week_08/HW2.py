# Loop through the above list (HW1) and print elements individually only if they are integers.


list = [1,12, 4.2, False,"Not imporant", True, "V.V.V.I.P", 42, 24.09, 63]

x = 0

for l in list:
    if type(list[x]) == int:
        print list[x]
        x = x + 1
    else:
        x = x + 1
