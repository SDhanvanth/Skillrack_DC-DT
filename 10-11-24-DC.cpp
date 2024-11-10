/*
-------> Zig-Zag Characters- Two String Values <-------------
The program must. accept two string values s1 and s2 of equal length as the input. The program must
print the characters from both s1 and s2 based on the following order.
1st character in s1, 2nd character in S2, 1st character in S2 and 2nd character in s1 are printed.
3rd character in s1, 4th character in S2, 3rd character in s2 and 4th character in s1 are printed.
5th character in s1, 6th character in S2, 5th character in s2 and 6th character in s1 are printed
Similarly, the remaining the characters are printed alternatively from both $1 and S2 as the output.
Note: The length of s1 and s2 are always even.
Boundary Condition(s):
2 <= Length of s1, s2 <= 1000
Input Format:
The first line contains S1.
The second line contains S2
Output Format:
The first line contains the characters from both s1 and s2 as per the given order.
Example Input/Output 1:
Input:
note
ball
Output:
nabotlle
*/
#include <bits/stdc++.h>
using namespace std;
int main(int argc, char** argv){
  string s1,s2;
  cin>>s1>>s2;
  int x = 1;
  for(int i = 0;i<s1.size();i++){
    cout<<s1[i++]<<s2[x--]<<s2[x]<<s1[i]<<"";
    x = i+2;
  }
}
