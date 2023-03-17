# lc 3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        charSet = set()
        leftPtr = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[leftPtr])
                leftPtr +=1

            charSet.add(s[r])
            result = max(result, r - leftPtr + 1)

        return result