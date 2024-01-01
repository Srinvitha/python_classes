import datetime
def is_prime(n, div=2):
    global primelist
    if div> n/2.0: return True
    if div < primelist[0]:
        div = primelist[0]
        for x in primelist:
            if x ==0 or x==1: continue
            if n % x == 0:
                return False
    if n% div == 0:
        return False
    else:
        div+=1
        return is_prime(n,div)


now = datetime.datetime.now()
print 'time and date:',now
until = 1000
primelist=[]
for i in range(until):
    if is_prime(i):
        primelist.insert(0,i)
print "There are", len(primelist),"prime numbers, until", until
print primelist[0:100], "..."

finish = datetime.datetime.now()
print "It took your computer", finish - now , " to calculate it"


OR 


import datetime
def is_prime(n, div=2):
    global primelist
    if div> n/2.0: return True
    if div < primelist[0]:
        div = primelist[0]
        for x in primelist:
            if x ==0 or x==1: continue
            if n % x == 0:
                return False
    if n% div == 0:
        return False
    else:
        div+=1
        return is_prime(n,div)


now = datetime.datetime.now()
print ('time and date:'),now
until = 700
primelist=[]
for i in range(until):
    if is_prime(i):
        primelist.insert(0,i)
print ("There are", len(primelist),"prime numbers, until", until)
print (primelist[0:100], "...")

finish = datetime.datetime.now()
print ("It took your computer", finish - now , " to calculate it")

