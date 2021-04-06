# bucket sort

测试地址 : https://leetcode-cn.com/problems/sort-an-array/

通过所有测试。

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums

        bucketsize = 10
        _min, _max = min(nums), max(nums)
        bucketnum = (_max - _min) // bucketsize + 1
        bucket = [[] * bucketnum]
        for each in nums:
            bucket[(each - _min) // bucketsize].append(each)

        res = []
        for each in bucket:
            res += sorted(each) # 可以使用任意的排序方法对每个桶内的元素进行排序
        return res
```