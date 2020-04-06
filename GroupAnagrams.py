"""
Given an array of strings, group anagrams together.

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""

class Solution:
    def groupAnagrams(self, strs):
        m = {}
        for i in strs:
            if ("".join(sorted(i)) in m.keys()):
                m["".join(sorted(i))].append(i)
            else:
                m["".join(sorted(i))] = [i]
                
        return list(m.values())