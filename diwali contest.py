probs=int(input())
tot=int(input())
c=0
s=0
rt=4*60-tot
for i in range(1,probs+1):
    s=s+5*i
    if s>rt:
        break
    c=c+1
print(c)