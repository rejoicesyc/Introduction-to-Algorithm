# heap sort
测试地址：https://leetcode-cn.com/problems/sort-an-array/

通过所有测试

1. 递归解法

```python
class Solution1:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heap_adjust(start: int, end: int) -> None:
            child = start * 2 + 1
            if child < end:
                tmp = child + 1

                # 下面的语句从两个叶子节点中选出大的与根节点作比较
                child = tmp if tmp < end and nums[child] < nums[tmp] else child

                if nums[child] > nums[start]:
                    nums[child], nums[start] = nums[start], nums[child]
                    heap_adjust(child, end)

        n = len(nums)

        # 从最底层的非叶子节点开始递归构造最大堆
        for i in range(n // 2 - 1, -1, -1):
            heap_adjust(i, n)
            
        for i in range(n - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heap_adjust(0, i)
        return nums
```

2. 迭代解法

```python
class Solution2:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heap_adjust(start: int, end: int) -> None:
            child = start * 2 + 1
            while child < end:
                tmp = child + 1
                child = tmp if tmp < end and nums[child] < nums[tmp] else child
                if nums[child] > nums[start]:
                    nums[child], nums[start] = nums[start], nums[child]
                    start = child
                    child = start * 2 + 1
                else:
                    break
                
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            heap_adjust(i, n)
        for i in range(n - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heap_adjust(0, i)
        return nums
```