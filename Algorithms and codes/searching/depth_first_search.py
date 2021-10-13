from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
	def addEdge(self, u, v):
		self.graph[u].append(v)
	def dfsH(self, v, visited):
		visited.add(v)
		print(v)
		for nextL in self.graph[v]:
			if nextL not in visited:
				self.dfsH(nextL, visited)
	def dfs(self, v):
		visited = set()
		self.dfsH(v, visited)
g = Graph()
g.addEdge('A','B')
g.addEdge('A', 'C')
g.addEdge('B', 'D')
g.addEdge('B', 'E')
g.addEdge('C', 'F')
g.addEdge('C', 'G')
g.addEdge('D', 'D')
g.addEdge('E', 'E')
g.addEdge('F', 'F')
g.addEdge('G', 'G')

g.dfs('A')

