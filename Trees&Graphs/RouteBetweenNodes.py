#Graph:
# 1- Directed
# 2- We're looking for path so BFS or DFS, but BFS find a path faster.
# 3- return True or False
class Graph:
    def __init__(self, root=None):
        self.nodes = dict()
    def add(self, data, children):
        self.nodes[data]=children
    def FindPathBFS(self, nodeA, nodeB):
        size = len(self.nodes)
        visited = [False]*size
        
        queue = []
        queue.append(nodeA)
        visited[nodeA] = True
        
        while (queue):
            currentNode = queue.pop(0)
            if (currentNode == nodeB):
                print("There is a path between ",nodeA,"and",nodeB,".")
                return True
            for child in self.nodes[currentNode]:
                if (visited[child] == False):
                    visited[child] = True
                queue.append(child)
        print("There is no path between ",nodeA,"and",nodeB,".")
        return False

    



myGraph = Graph()
myGraph.add(0,[])
myGraph.add(1,[2])
myGraph.add(2,[0,3])
myGraph.add(3,[0])
myGraph.FindPathBFS(0,1)
