"""Given a binary matrix, print all unique rows of the given matrix"""
l=[]
a=int(input())
for i in range(a):
     r=list(map(str,input().split()))
     l.extend([r])
d=[]
s=" "
for i in range(len(l)):
     m=l[i]
     k=s.join(l[i])
     if k not in d:
          print(l[i])
          d.append(k)
