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
        支持负数的排序
        tmp 数组用于记录当前位数字，从 -9 到 9，一共 19 种
        [ 0 ...... 9 ...... 18 ]
          -9 ~ -1  0   1 ~ 9
        """

        mod, div = 10, 1
        for i in range(digit):
            for each in nums:
                if each < 0: # 负数情况，因为 python 负数 // 运算同样是向下取整，可以取绝对值后再取模
                    tmp[9 - abs(each) % mod // div].append(each)
                else:
                    tmp[each % mod // div + 9].append(each)

            nums = [x for each in tmp for x in each]  # 相当于按顺序合并 tmp 数组的所有元素
            mod, div, tmp = mod * 10, div * 10, [[] for _ in range(19)]
        return nums
```