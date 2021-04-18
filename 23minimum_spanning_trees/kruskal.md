# kruskal

测试地址：https://leetcode-cn.com/problems/min-cost-to-connect-all-points/

通过所有测试

```python
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # 输入邻接矩阵 g，返回最小生成树的路径和
        def kruskal(g: List[List[int]]) -> int:
            g = sorted(g, key=lambda x:x[2])
            parent = list(range(n))
            def find(x: int) -> int:
                if x != parent[x]:
                    parent[x] = find(parent[x])
                return parent[x]

            res = 0
            for i, j, w in g:
                a, b = find(i), find(j)
                if a != b:
                    parent[a] = b
                    res += w
            return res

        g = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                g.append((i, j, abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])))   
        return kruskal(g)
```