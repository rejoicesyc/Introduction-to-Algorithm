# radix sort

测试地址 : https://leetcode-cn.com/problems/sort-an-array/

通过所有测试

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        digit = len(str(max([abs(each) for each in nums])))

        tmp = [[] for _ in range(19)]
        """
        tmp 数组用于记录当前位数字，从 -9 到 9，一共 19 种
        [ 0 ...... 9 ...... 18 ]
          -9 ~ -1  0   1 ~ 9
        """

        mod, div = 10, 1
        for i in range(digit):
            for each in nums:
                if each < 0:
                    tmp[9 - abs(each) % mod // div].append(each)
                else:
                    tmp[each % mod // div + 9].append(each)

            nums = []
            for each in tmp:
                nums += each
            
            mod, div, tmp = mod * 10, div * 10, [[] for _ in range(19)]
        return nums
```