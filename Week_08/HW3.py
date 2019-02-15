# Slice the tuple at places where you find a type change.


tuple = 1,12, 4.2, False,"Not imporant", True, "V.V.V.I.P", 42, 24.09, 63

x = 0

for t in tuple:
    if type(tuple[x]) != int:
        slice(tuple)
        print(tuple)
        x = x + 1
    else:
        x = x + 1


