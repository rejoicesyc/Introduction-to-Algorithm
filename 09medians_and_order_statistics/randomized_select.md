# randomized select

测试地址：https://leetcode-cn.com/problems/kth-largest-element-in-an-array/

通过所有测试

书上的要求是返回第 k 小，题目是第 k 大，需要做一步转换。

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def RandomizedPartition(left: int, right: int) -> int:
            key_index = random.randint(left, right)
            nums[key_index], nums[left] = nums[left], nums[key_index]
            key = nums[left]
            i = left - 1
            for j in range(left, right + 1):
                if nums[j] <= key:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[left], nums[i] = nums[i], nums[left]
            return i

        def RandomizedSelect(left: int, right: int) -> int:
            pivot = RandomizedPartition(left, right)
            if pivot == k: return nums[pivot]
            elif pivot < k: return RandomizedSelect(pivot + 1, right)
            elif pivot > k: return RandomizedSelect(left, pivot - 1)

        k = len(nums) - k
        return RandomizedSelect(0, len(nums) - 1)
```