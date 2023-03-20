# lc 605
class Solution:
    def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
        flowers = [0] + flowerbed + [0] #adding 0 on the edges of the array
        
        for i in range(1, len(flowers) - 1): #skip the first and last zero added in
            if flowers[i - 1] == 0 and flowers[i] == 0 and flowers[i + 1] == 0:
                flowers[i] = 1
                n -= 1
        return n <=0