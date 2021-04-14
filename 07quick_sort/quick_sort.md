# quick sort
测试地址：https://leetcode-cn.com/problems/sort-an-array/

通过所有测试

1. 选择了中间的数作为 pivot

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(left: int, right: int) -> None:
            if left >= right:
                return 
            i, j = left, right
            mid = nums[(left + right) // 2]
            while i <= j:
                while nums[j] > mid:
                    j -= 1
                while nums[i] < mid:
                    i += 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            quick_sort(left, j)
            quick_sort(i, right)

        quick_sort(0, len(nums) - 1)
        return nums
```