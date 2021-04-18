# prim

测试地址：https://leetcode-cn.com/problems/min-cost-to-connect-all-points/

通过所有测试

1. 邻接矩阵的 prim 算法

```python
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # 输入邻接矩阵 g，输出最小生成树的路径和
        def prim(g: List[List[int]]) -> int:
            visit = [1] + [0] * (n - 1)
            dis = [float('inf')] + [g[0][i] for i in range(1, n)]
            ret = 0
            for _ in range(n - 1):
                min_tmp = -1
                for i in range(n):
                    if visit[i] == 0 and (min_tmp == -1 or dis[min_tmp] > dis[i]):
                        min_tmp = i 
                visit[min_tmp] = 1
                ret += dis[min_tmp]
                dis[min_tmp] = float('inf')
                for i in range(n):
                    dis[i] = min(dis[i], g[min_tmp][i])
            return ret

        n = len(points)
        g = [[abs(x[0] - y[0]) + abs(x[1] - y[1]) for x in points] for y in points]
        return prim(g)
```