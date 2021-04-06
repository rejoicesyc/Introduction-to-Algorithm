# quick sort
测试地址：https://leetcode-cn.com/problems/sort-an-array/

通过所有测试

1. 第一个版本选择了最左边的数作为 pivot

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(left: int, right: int) -> None:
            if left >= right:
                return
            pivot, i, j = nums[left], left, right
            while i < j:
                while i < j and nums[j] >= pivot:
                    j -= 1
                while i < j and nums[i] <= pivot:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[left], nums[j] = nums[j], nums[left]
            quickSort(left, j - 1)
            quickSort(j + 1, right)

        quickSort(0, len(nums) - 1)
        return nums
```