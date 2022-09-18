from collections import defaultdict as d


class Graph:
    def __init__(self):
        self.graph = d(list)

    def addEdge(self, src, dest):
        self.graph[src].append(dest)

    def BFS(self, Start):
        queue = []
        queue.append(Start)
        visited = [False] * (max(self.graph) + 1)
        print("Visited Nodes")
        print(visited)
        while queue:
            v = queue.pop(0)
            print(v, " Node reach")

            for i in self.graph[v]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i]=True


if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    g.BFS(1)
    print(g.graph)