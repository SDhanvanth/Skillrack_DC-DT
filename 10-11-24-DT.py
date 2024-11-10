"""
------> Super Substring <-------
The program must accept N string values as the input.If a string is a substring of another string among the
N string values, then it is a super substring. The program must print the super substring values among the
given N string values as the output. If there is no super substring. the program must print -1 as the output.
Boundary Condition(s):
2 <= N <= 100
1 <= Length of each string <= 100
Output Format:
The lines containing the super substrings among the given N string values or the first line contains -1.
Example Input/Output 1:
Input:
art
moon
artist
on
moonwalk
Output:
art
moon
on
"""
n = int(input())
val = list()
flag = 0
for i in range(n):
  ele = input().strip()
  val.append(ele)
for i in range(0,len(val)):
  for j in range(0,len(val)):
    if (val[i] in val[j]) and i!=j:
      print(val[i])
      flag+=1
      break
if flag == 0:
  print(-1)
