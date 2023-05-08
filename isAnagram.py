# lc 242
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # base case where both s and t must be same length
        if len(s) != len(t):
            return False
        # empty hashmaps/dictionaries
        sCount = {}
        tCount = {}
        # going through strings and incrementing the count of letter by 1
        # using get, so that if theres no value, it returns 0
        for i in range(len(s)):
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            tCount[t[i]] = 1 + tCount.get(t[i], 0)
        # iterate through hashmap and count the keys
        for c in sCount:
            if sCount[c] != tCount.get(c,0 ):
                return False
        return True
    
    def isAnagram(self, s: str, t: str) -> bool:
        # code sorts strings in alphabetical order and compares
        return sorted(s) == sorted(t)
    