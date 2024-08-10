def findCheapestPrice(n, flights, src, dst, k):
    # Initialize distances array
    dist = [float('inf')] * n
    dist[src] = 0
    
    # Relax edges up to k+1 times
    for _ in range(k + 1):
        new_dist = dist[:]
        for u, v, w in flights:
            if dist[u] != float('inf') and dist[u] + w < new_dist[v]:
                new_dist[v] = dist[u] + w
        dist = new_dist
    
    return dist[dst] if dist[dst] != float('inf') else -1

# Example usage
n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1
print(findCheapestPrice(n, flights, src, dst, k))  # Output: 700
