# insertion sort

测试地址 https://leetcode-cn.com/problems/sort-an-array/

通过 10 / 11 的测试，最后一例超时

```python
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
```