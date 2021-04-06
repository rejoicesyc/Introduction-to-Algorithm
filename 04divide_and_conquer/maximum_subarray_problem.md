# maximum subarray problem

买卖股票的最佳时机测试 https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

最大子序和测试 https://leetcode-cn.com/problems/maximum-subarray/

虽然书中提出的是股票问题，但是书中的解法是求出两天之间票价的插值，转化成求最大子序和问题。
下面给出原题解法和通过最大子序和求解的方法

每个问题中 maxProfit 函数调用解决买卖股票问题， maxSubArray 函数解决最大子数组问题，其他函数为辅助函数。

## 暴力算法

通过了最大子序和 202 / 203 的测试例，最后一例超时

通过了股票问题 198 / 210 的测试例，最后超时

```python
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        res, n = - float('inf'), len(nums)
        for i in range(n):
            tmp = nums[i]
            if tmp > res:
                res = tmp
            for j in range(i + 1, n):
                tmp += nums[j]
                if tmp > res:
                    res = tmp
        return res

    def maxProfit(self, prices: List[int]) -> int:
        changes = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
        return max(self.maxSubArray(changes), 0)
```

## 分治法

通过了最大子序和， 买卖股票问题的所有测试

```python
class Solution2:
    def maxCrossingSubarray(self, nums: List[int]) -> None:
        n = len(nums)
        mid = n // 2

        res1, tmp = - float('inf'), 0
        for i in range(mid - 1, -1, -1):
            tmp += nums[i]
            res1 = max(res1, tmp)

        res2, tmp = - float('inf'), 0
        for i in range(mid, n):
            tmp += nums[i]
            res2 = max(res2, tmp)

        return res1 + res2

    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        else:
            mid = n // 2
            return max(self.maxSubArray(nums[:mid]), self.maxSubArray(nums[mid:]), self.maxCrossingSubarray(nums))

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # 求最大子数组函数不能接收空数组输入
        if n == 1:
            return 0

        changes = [prices[i] - prices[i - 1] for i in range(1, n)]
        return max(self.maxSubArray(changes), 0)
```

## 比较好的子数组和解法

通过子数组所有测试

通过股票问题 198 / 210 的测试

解释：因为这个例子是 range(10000, -1, -1) 的数组，所以在求changes和后面动态规划的时候遍历了两遍时间太长不能通过。

```python
class Solution3:
    def maxSubArray(self, nums: List[int]) -> int:
        pre, res = 0, nums[0]
        for i in nums:
            pre, res = max(pre + i, i), max(pre, res)
        return res

    def maxProfit(self, prices: List[int]) -> int:
        changes = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
        return max(self.maxSubArray(changes), 0)
```

## 股票问题的解法

通过股票问题所有测试

```python
class Solution4:
    def maximum_subarray(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float('inf')

        for price in prices:
            min_price, max_profit = min(min_price, price), max(price - min_price, max_profit)

        return max_profit
```