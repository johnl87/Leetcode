#lc 771

jewels = "aA"
stones = "aAAbbbb"

def numJewelsIsInStones(jewels, stones):
    set1 = set(jewels)
    answer = 0
    for i in stones:
        if i in set1:
            answer +=1
    return answer