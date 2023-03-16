class Solution:
    def reverseNum(x)-> int:
        # convert number to string
        numToString = str(x)
        
        # check if string/number character at 0 is negative
        if numToString[0] == '-':
            return int('-' + numToString[:0:-1])
        else:
            return int(numToString[::-1])
        
    print(reverseNum(-123))