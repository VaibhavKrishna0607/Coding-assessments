x = int(input())
s = str(abs(x))
rev = int(s[::-1])

if x<0:
    rev = -rev
if rev<-2**31 or rev>2**31-1:
    print(0)
else:print(rev)


#120
#21