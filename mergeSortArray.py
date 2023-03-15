# lc 88
class Solution:
    def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m::1]=nums2[::1]
        nums1.sort()
        print(nums1)
    merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
