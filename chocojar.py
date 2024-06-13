a=list(map(int,input().split()))
n=int(input())
c=0
for i in a:
    b=i//n
    if b%n==0:
     b=b+1
     c=c+b
    else:
     c=c+b
print(c)