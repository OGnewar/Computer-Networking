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
