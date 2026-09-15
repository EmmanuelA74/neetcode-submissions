class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(node):
            if node in visiting:
                return False    #cycle detected
            if node in visited:
                return True
            
            visiting.add(node)

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            
            visiting.remove(node)
            visited.add(node)

            return True

        #build graph
        graph = defaultdict(list)

        for x, y in prerequisites:
            graph[y].append(x)
        
        visited = set()
        visiting = set() 

        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return False
        
        return True