import math 
n=int(input())
k=0
for i in range(2, int(math.sqrt(n)) + 1):
     c=0
     while (n%i==0):  
       c+=1
       n=n//i
     if (c>0):
          k=1
          print(i,c)
if k==0:
     print(n,1)
