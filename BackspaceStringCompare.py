"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

"""

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = []
        for i in range(len(S)):
            if S[i]!="#":
                s.append(S[i])
            else:
                if len(s)!=0:
                    s.pop(-1)
        
        t = []
        for i in T:
            if i!="#":
                t.append(i)
            else:
                if len(t)!=0:
                    t.pop(-1)
        
        if "".join(s) == "".join(t):
            return True
        else:
            return False