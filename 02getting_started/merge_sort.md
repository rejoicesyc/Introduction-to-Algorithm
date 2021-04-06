# merge sort

测试地址 : https://leetcode-cn.com/problems/sort-an-array/ 

通过所有测试

```python
class Solution:
    def merge(self, left: List[int], right: List[int]) -> None:
        res, i, j = [], 0, 0
        n_left, n_right = len(left), len(right)
        while i < n_left and j < n_right:
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        return res + left[i:] + right[j:]
        
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2:
            return nums
        
        mid = n // 2
        return self.merge(self.sortArray(nums[:mid]), self.sortArray(nums[mid:]))
```