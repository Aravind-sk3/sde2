"""In this problem the input will consist of a number of lines of English text consisting of the letters of the English alphabet, the punctuation marks ' (apostrophe), . (full stop), , (comma), ; (semicolon), :(colon) and white space characters (blank, newline). Your task is print the words in the text in reverse order without any punctuation marks.
For example consider the following candidate for the input text:
  This is a sample piece of text to illustrate this 
  problem.  If you are smart you will solve this right.
The corresponding output would read as:
  right this solve will you smart are you If problem
  this illustrate to text of piece sample a is This
That is, the lines are printed in reverse order and in each line the words are printed in reverse order."""
p= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
s=input()
m=''
for char in s:
   if char not in p:
       m=m+ char
l=list(map(str,m.split()))
print(' '.join(l[::-1]))
