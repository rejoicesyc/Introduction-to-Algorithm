from typing import List

class Solution:
    def insert_sort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1, n):
            j = i 
            key = nums[j]
            while j > 0 and key < nums[j - 1]:
                nums[j] = nums[j - 1]
                j -= 1
            nums[j] = key
        return nums