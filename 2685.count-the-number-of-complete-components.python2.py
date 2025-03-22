# @leet start
class Solution:
    def countCompleteComponents(self, n, edges):
        # Create adjacency list representation of the graph
        graph = [[] for _ in range(n)]

        # Build graph from edges
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        complete_components = 0

        # Process each unvisited vertex
        for vertex in range(n):
            if not visited[vertex]:
                # BFS to find all vertices in the current component
                component = []
                queue = [vertex]
                visited[vertex] = True

                while queue:
                    current = queue.pop(0)
                    component.append(current)

                    # Process neighbors
                    for neighbor in graph[current]:
                        if not visited[neighbor]:
                            queue.append(neighbor)
                            visited[neighbor] = True

                # Check if component is complete (all vertices have the right number of edges)
                is_complete = True
                for node in component:
                    if len(graph[node]) != len(component) - 1:
                        is_complete = False
                        break

                if is_complete:
                    complete_components += 1

        return complete_components


# @leet end
sol = Solution()
n = 6
edges = [[0, 1], [0, 2], [1, 2], [3, 4]]
print(sol.countCompleteComponents(n, edges))
