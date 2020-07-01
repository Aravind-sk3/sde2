
"""
As we all know, a palindrome is a word that equals its reverse. Here are some examples of palindromes: malayalam, gag, appa, amma.
We consider any sequence consisting of the letters of the English alphabet to be a word. So axxb,abbba and bbbccddx are words for our purpose. And aaabbaaa, abbba and bbb are examples of palindromes.
By a subword of a word, we mean a contiguous subsequence of the word. For example the subwords of the word abbba are a, b, ab, bb, ba, abb, bbb, bba, abbb, bbba and abbba.
In this task you will given a word and you must find the longest subword of this word that is also a palindrome.
For example if the given word is abbba then the answer is abbba. If the given word is abcbcabbacba then the answer is bcabbacb"""
n = int(input())
s = input()
t= ""
for i in range(len(s)):
     for j in range(len(s)-1,i-1,-1):
          if s[i]==s[j]:
               m = s[i:j+1]
               if m == m[::-1]:
                    if len(t) <= len(m):
                         t = m
print(len(t))
print(t)
