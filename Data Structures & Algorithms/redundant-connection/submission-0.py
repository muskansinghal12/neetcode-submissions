class Solution:
    def find(self, parent, x):
        if parent[x] == x:
            return x
        parent[x] = self.find(parent,parent[x])
        return parent[x]
    def union(self, parent, rank, x, y):
        x_parent = self.find(parent,x)
        y_parent = self.find(parent,y)
        if x_parent == y_parent:
            return True
        elif rank[x_parent] > rank[y_parent]:
            parent[y_parent] = x_parent
        elif rank[y_parent] > rank[x_parent]:
            parent[x_parent] = y_parent
        else:
            parent[x_parent] = y_parent
            rank[y_parent] += 1
        return False
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [0]*(n+1)
        for u,v in edges:
            if self.union(parent, rank, u,v):
                return [u,v]
        return []
        

        