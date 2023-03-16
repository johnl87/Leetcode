class Solution:
    def longestCommonPrefix(strs: list[str]) -> str:
        result = ""

        prefix = strs[0]
        #print(prefix)

        for item in strs[1:]:
            while item[:len(prefix)] != prefix and prefix:
                prefix = prefix[:len(prefix) -1]
            if not prefix:
                break
        result = prefix
        return result
       