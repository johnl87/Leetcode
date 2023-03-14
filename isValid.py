class Solution:
    def isValid(s: str) -> bool:
        char = []
        d = {'(':')', '[':']','{':'}'}
        for input in s:
            if input in d:
                char.append(input)
            elif len(char) == 0 or d[char.pop()] != input:
                return False
        return not char

    print(isValid("()[]"))