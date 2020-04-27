n= 1
v= 0
while v<1000:
    n = n+1
    if n%2==0:
        if n==2:
            print "2 is prime"
    else:
        for r in range(2,n):
            if n%r !=0:
                print n
                v = v+1
                break

        
