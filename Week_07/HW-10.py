# 10. Given a list of numbers, print the maximum number in the list.


a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
a.sort()
print "Largest element is:","\n",a[n-1]



