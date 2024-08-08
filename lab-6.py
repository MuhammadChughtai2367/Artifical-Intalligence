

# Graph Class
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, v, w):
        self.graph[v].append(w)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                self.DFSUtil(neighbour, visited)
    
    def DFS(self, v):
        visited = [False] * self.V
        self.DFSUtil(v, visited)


# Main program to create a graph and perform DFS
if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Following is the Depth First Traversal (starting from vertex 2)")
    g.DFS(2)


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, v, w):
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(w)

    def DFS(self, start):
        visited = set()
        stack = [start]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex, end=' ')
                visited.add(vertex)
                for neighbour in reversed(self.graph.get(vertex, [])):
                    if neighbour not in visited:
                        stack.append(neighbour)


# Main program
if __name__ == "__main__":
    # Creating the graph
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'D')
    g.add_edge('A', 'E')
    g.add_edge('B', 'K')
    g.add_edge('B', 'J')
    g.add_edge('K', 'N')
    g.add_edge('K', 'M')
    g.add_edge('E', 'C')
    g.add_edge('E', 'H')
    g.add_edge('E', 'I')
    g.add_edge('I', 'L')
