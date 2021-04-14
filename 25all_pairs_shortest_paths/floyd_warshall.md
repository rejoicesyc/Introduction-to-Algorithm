# floyd warshall 

测试地址：https://leetcode-cn.com/problems/network-delay-time/

通过所有测试


1. 邻接矩阵的 floyd 算法

```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # 返回整个矩阵，矩阵元素 g[i][j] 表示有向边 i -> j 的最短路径
        def floyd(g: List[List[int]]) -> List[List[int]]:
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        g[i][j] = min(g[i][j], g[i][k] + g[k][j])
            return g

        g = [[float('inf')] * n for _ in range(n)]
        for u, v, w in times:
            g[u - 1][v - 1] = w
        for i in range(n):
            g[i][i] = 0
        ret =  max(floyd(g)[k - 1])
        return ret if ret != float('inf') else -1
```