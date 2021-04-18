# bellman ford

测试地址：https://leetcode-cn.com/problems/network-delay-time/

通过所有测试

1. 邻接表的 bellman_ford 算法

```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # 因为要遍历所有的边，bellman_ford 算法使用邻接矩阵比较方便，g 表示邻接矩阵
        # 输出如果为 None 表示存在负权边回路
        def bellman_ford(g: List[List[int]], k: int):

            # 因为题目输入的节点名称为 1...n，所以使用 n + 1 维的 dis 数组更方便
            # 要注意将 dis[0] 和 dis[k] 置零
            dis = [float('inf')] * (n + 1)
            dis[k] = dis[0] = 0

            edge_num = len(g)
            for _ in range(n):
                for i in range(edge_num):
                    dis[g[i][1]] = min(dis[g[i][1]], dis[g[i][0]] + g[i][2])
            for i in range(edge_num):
                if dis[g[i][1]] > dis[g[i][0]] + g[i][2]:
                    return None
            return dis
        
        dis = bellman_ford(times, k)
        if dis != None:
            ret = max(dis)
            return ret if ret != float('inf') else -1
        else:
            return -1
```