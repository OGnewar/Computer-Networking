## Tasks:
```
1. On leetcode.com find a problem for Dijkstra algorithm then solve it on a preferred programming language.
2. Do the same as above, but for Bellman Ford algorithm.
```
# 1. On leetcode.com find a problem for Dijkstra algorithm then solve it on a preferred programming language.

## Network Delay Time

You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (ui, vi, wi)`, where `ui` is the source node, `vi` is the target node, and `wi` is the time it takes for a signal to travel from source to target.

We will send a signal from a given node `k`. Return the minimum time it takes for all the `n` nodes to receive the signal. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

Example 1:
<img src="01.png">

Input: `times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2`
Output: `2`

Example 2:

Input: `times = [[1,2,1]], n = 2, k = 1`
Output: `1`

Example 3:

Input: `times = [[1,2,1]], n = 2, k = 2`
Output: `-1`

Constraints:

- `1 <= k <= n <= 100`
- `1 <= times.length <= 6000`
- `times[i].length == 3`
- `1 <= ui, vi <= n`
- `ui != vi`
- `0 <= wi <= 100`
- All the pairs `(ui, vi)` are unique. (i.e., no multiple edges.)

```
import heapq
from collections import defaultdict
import sys

def networkDelayTime(times, n, k):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    
    min_heap = [(0, k)]
    dist = {i: sys.maxsize for i in range(1, n+1)}
    dist[k] = 0
    
    while min_heap:
        curr_dist, node = heapq.heappop(min_heap)
        if curr_dist > dist[node]:
            continue
        
        for neighbor, time in graph[node]:
            new_dist = curr_dist + time
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbor))
    
    max_dist = max(dist.values())
    return max_dist if max_dist < sys.maxsize else -1

# Example usage
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
print(networkDelayTime(times, n, k))  # Output: 2
```

## Explanation:

- We use a priority queue (min-heap) to always expand the node with the smallest known distance.

- We track the shortest path to each node using Dijkstra's algorithm.

- Finally, we check the maximum distance from the starting node `k` to all other nodes.

This solution efficiently computes the minimum time required for the signal to reach all nodes or determines that it is not possible.