l = [2, 4.2,True, "Tom"]
print(l)
l[0] = 5
print(l)
t = (2,4,False,"Jerry")
print(t)
#t[0] = 5
#print(t)

print("\n")

c = [2.4, 242, False,eval,-63,-4.932, "collection",float, sum , "Yellow"]
print(c[0])
print(c[1])
print(c[2])
print(c[3])
print(c[4])
print(c[5])
print(c[6])
print(c[7])
print(c[8])
print(c[9])
print(c)

print("\n")

ct = (2.4, 242, False,eval,-63,-4.932, "collection",float, sum , "Yellow")
print(ct[0])
print(ct[1])
print(ct[2])
print(ct[3])
print(ct[4])
print(ct[5])
print(ct[6])
print(ct[7])
print(ct[8])
print(ct[9])
print(ct)

print("\n")

nl = [0,1,2,3,4,5,6,7,8,9,10,11,12]
nl[7]=(nl[0]+nl[4])//2
nl[9]=(nl[12]//nl[6])*3
print(nl)
nl[3],nl[5],nl[11] = (input("Enter a,b,c :"))
print(nl)

for l in nl:
    print(l)

n =(len(nl))
for m in range(len(nl) -1,-1,-1):
    print(nl[m])

print("\n")

#nt = (0,1,2,3,4,5,6,7,8,9,10,11,12)
#nt[7]=(nt[0]+nt[1])/2
#nt[9]=(nt[12]/nt[6])*3
#print(nt)
#nt[3],nt[5],nt[11] = eval(input("Enter a,b,c :"))
#print(nt)
#
#for t in nt:
#   print(t)

def make_list():
    '''
    Builds a list from input provided by the user.
    '''
    result = []         # List to return is initially empty.
    in_val = 0          # Ensure loop is entered at least once.
    while in_val >= 0:
        in_val = (input("Enter integer (negative integer quits continuing the list.): "))
        if in_val >= 0:
            result = result + [in_val]
    return result

def main():
    col = make_list()
    print(col)
main()
