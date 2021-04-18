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

2. 加入随机版本的快排

```python
class Solution:
    def randomized_partition(self, nums, l, r):
        pivot = random.randint(l, r)
        nums[pivot], nums[r] = nums[r], nums[pivot]
        i = l - 1
        for j in range(l, r):
            if nums[j] < nums[r]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    def randomized_quicksort(self, nums, l, r):
        if r - l <= 0:
            return
        mid = self.randomized_partition(nums, l, r)
        self.randomized_quicksort(nums, l, mid - 1)
        self.randomized_quicksort(nums, mid + 1, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.randomized_quicksort(nums, 0, len(nums) - 1)
        return nums
```