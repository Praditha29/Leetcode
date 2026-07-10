#LEETCODE PROBLEM 3558: NUMBER OF WAYS TO ASSIGN EDGE WEIGHTS 
class Solution:
    def assignEdgeWeights(self, edges):
        from collections import defaultdict
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        def dfs(node):
            visited.add(node)
            count = 1
            for neighbor in graph[node]:
                if neighbor not in visited:
                    count += dfs(neighbor)
            return count
        
        total_ways = 1
        for node in graph:
            if node not in visited:
                component_size = dfs(node)
                total_ways *= 2 ** (component_size - 1)
        
        return total_ways
# Example usage:
edges = [[1,2]]
solution = Solution()
print(solution.assignEdgeWeights(edges))  # Output: 2