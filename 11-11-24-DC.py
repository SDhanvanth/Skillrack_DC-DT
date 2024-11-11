"""
------> Find Reversed Substring <---------
The program must accept two string values S1 and S2 as the input. 
The string values S1 and S2 are always the same, but one substring of S2 is reversed in S1. 
The program must find that substring in S2 and print it as the output.
Boundary Condition(s):
2 <= Length of S1, S2 <= 100
Input Format:
The first line contains S1.
The second line contains S2.
Output Format:
The first line contains the substring of S2 which is reversed in S1.
Example Input/Output 1:
Input:
SkaRllick
SkillRack
Output:
illRa
Explanation:
Here S1 = "SkaRllick" and S2 = "SkillRack".
The substring illRa in S2 is reversed in S1.
So illRa is printed as the output.
"""
s1 = input().strip()
s2 = input().strip()
for i in range(len(s1)):
  if s1[i]!=s2[i]:
    s = i
    break
j = len(s1)-1
while j>=0:
  if s1[j] != s2[j]:
    e = j
    break
  j -= 1
print(s2[s:e+1])
