# counting sort

测试地址 : https://leetcode-cn.com/problems/sort-an-array/

通过所有测试。

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        _min, _max = min(nums), max(nums)
        tmp = [0] * (_max - _min + 1)
        for each in nums:
            tmp[each - _min] += 1

        res = []
        for i, each in enumerate(tmp):
            for _ in range(each):
                res.append(i + _min)

        return res
```