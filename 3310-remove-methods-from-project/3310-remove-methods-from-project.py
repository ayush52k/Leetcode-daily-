from collections import deque, defaultdict

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in invocations:
            graph[u].append(v)
        
        # 1. Find all suspicious methods using BFS starting from k
        suspicious = {k}
        queue = deque([k])
        
        while queue:
            curr = queue.popleft()
            for neighbor in graph[curr]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)
                    
        # 2. Check if any non-suspicious method invokes a suspicious method
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))
                
        # 3. Return all non-suspicious methods
        return [i for i in range(n) if i not in suspicious]