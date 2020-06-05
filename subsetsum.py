from itertools import combinations
n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=0
for i in range(1,n+1):
    for j in (combinations(l,i)):
        if sum(j)>=k:
            c+=1
print(c)
