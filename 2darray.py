a=[]
j=0
for i in range(0,2):
    sub=[]
    for j in range(0,2):
        ele=int(input())
        sub.append(ele)
    a.append(sub)
    print(a)
d={}
ans=[]
for i in range(0,2):
    for j in range(0,2):
        if a[i][j] not in d:
            d[a[i][j]]=1
        else:
            d[a[i][j]]+=1
            if d[a[i][j]]==2:
                ans.append(a[i][j])
print(d)
for i in range(0,10):
    if i not in d:
        ans.append(i)
print(d)
print(ans)