"""Ish and Govi are playing with strings. In this game Ish gives Govi two strings, aa and bb. Govi has to modify the string aa, such that it doesnot contain any character from string bb. Govi has to go to meet Omi. Help Govi to modify the string aa"""
a=list(map(str,input().split()))
b=list(map(str,input().split()))
d=''
for i in a:
     if i not in b:
          d=d+i
print(d)
