"""Write an efficient program to find the sum of contiguous subarray within a one-dimensional array of numbers which has the largest sum"""
l=list(map(int,input().split()))
m=l[0]
c=l[0]
for i in range(1,len(l)):
     c=max(l[i],c+l[i])
     m=max(m,c)
print(m)
