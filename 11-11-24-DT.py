"""
-------> Words Suggestion <----------
The program must accept N string values and a string S as the input. The N string values represent the words present in a text document. 
The string S is a word to be typed in the text document. The text document is opened in a text editor which suggests the words among the N words after each character of S is typed. 
The suggested words should have a common prefix with the word S. The program must print the suggested words after each character of S is typed. The suggested words must be printed in sorted order. 
If there are no words to suggest, the program must print -1.
Boundary Condition(s):
1 <= N <= 50
1 <= Length of each string <= 30
Input Format:
The first line contains N.
Output Format:
The lines, each contains the string values representing the suggested words or -1.
Example Input/Output 1:
Input:
8
monsoon
moonlight
mute
monday
make
monks
Output:
make monday monks monochrome monsoon monster moonlight mute monday monks monochrome monsoon monster moonlight
monday monks monochrome monsoon monster
monochrome
Explanation:
Here S = mono.
After typing the 1st character m, the suggested words are make, monday, monks, monochrome, monsoon, monster, moonlight and mute.
After typing the 2nd character o, the suggested words are monday, monks, monochrome, monsoon, monster and moonlight.
After typing the 3rd character n, the suggested words are monday, monks, monochrome,
monsoon and monster.
After typing the 4th character o, the suggested word is monochrome.
Hence the output is
make monday monks monochrome monsoon monster moonlight mute monday monks monochrome monsoon monster moonlight
monday monks monochrome monsoon monster
monochrome
"""
n = int(input())
text = list()
for i in range(n):
  ele = input().strip()
  text.append(ele)
text.sort()
word = list(input())
ref = ""
for i in word:
  ref += i
  flag = 0
  for j in text:
    if j.startswith(ref):
      flag+=1
      print(j,end=" ")
  if flag == 0:
    print(-1)
  else:
    print()
