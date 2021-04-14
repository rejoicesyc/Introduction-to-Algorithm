# dijkstra

测试地址：https://leetcode-cn.com/problems/network-delay-time/

通过所有测试

1. 邻接矩阵的 dijkstra 算法

```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # 输入邻接矩阵 g，输出列表 dis，dis[i] 表示 k 点到 i 点最短路径距离
        def dijkstra(g: List[List[int]], k: int) -> List[int]:
            v = [0] * n
            v[k] = 1
            dis = [g[k][i] for i in range(n)]
            dis[k] = 0
            for i in range(n - 1):
                min_index = -1
                for j in range(n):
                    if v[j] == 0 and (min_index == -1 or dis[j] < dis[min_index]):
                        min_index = j
                v[min_index] = 1
                for j in range(n):
                    dis[j] = min(dis[j], dis[min_index] + g[min_index][j])
            return dis
                
        g = [[float('inf')] * n for _ in range(n)]
        for u, v, w in times:
            g[u - 1][v - 1] = w
        ret =  max(dijkstra(g, k - 1))
        return ret if ret != float('inf') else -1
```