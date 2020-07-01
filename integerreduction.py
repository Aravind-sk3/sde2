a,b=map(int,input().split())
for i in range(b):
     if a%10==0:
          a=a//10
     else:
          a=a-1
print(a)
"""Little Praneet loves experimenting with algorithms and has devised a new algorithm. The algorithm is performed on an integer as follows:
•	if the rearmost digit is 0, he will erase it.
•	else, he will replace the rearmost digit dd with d−1.
If a point comes when the integer becomes 00, the algorithm stops.
You are given an integer n. Praneet will perform the algorithm on it aa times. You have to print the result after aa operations.
"""
