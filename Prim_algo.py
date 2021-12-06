import sys

class Graph:
    def __init__(self, vertices):
        self.vertice = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def add_edge(self, src = 0, dest = 0, length = 0):
        self.graph[src][dest] = length

    def print_solution(self, parent):
        for i in range(1, self.vertice):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def minKey(self, key, mstSet):

        min_value = sys.maxsize

        for v in range(self.vertice):
            if key[v] < min_value and mstSet[v] == False:
                min_value = key[v]
                min_index = v

        return min_index

    def primMST(self, node):

        key = [sys.maxsize] * self.vertice
        parent = [None] * self.vertice
        key[node] = 0
        mstSet = [False] * self.vertice

        parent[node] = -1

        for cout in range(self.vertice):

            u = self.minKey(key, mstSet)

            mstSet[u] = True

            for v in range(self.vertice):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_solution(parent)
        return mstSet


if __name__ == '__main__':
    g = Graph(5)
    g.add_edge(0, 1, 3)
    g.add_edge(0, 2, 224)
    g.add_edge(0, 3, 5)
    g.add_edge(0, 4, 15)
    g.add_edge(1, 0, 8)
    g.add_edge(1, 2, 33)
    g.add_edge(1, 3, 22)
    g.add_edge(1, 4, 18)
    g.add_edge(2, 0, 7)
    g.add_edge(2, 3, 53)
    g.add_edge(2, 4, 13)
    g.add_edge(2, 1, 14)
    g.add_edge(3, 1, 123)
    g.add_edge(3, 2, 21)
    g.add_edge(3, 4, 14)
    g.add_edge(3, 0, 5)
    g.add_edge(4, 0, 12)
    g.add_edge(4, 1, 2)
    g.add_edge(4, 2, 44)
    g.add_edge(4, 3, 32)

    # g.graph = [[0, 2, 0, 6, 0],
    #            [2, 0, 3, 8, 5],
    #            [0, 3, 0, 0, 7],
    #            [6, 8, 0, 0, 9],
    #            [0, 5, 7, 9, 0]]

    # g.add_edge(0, 19, 5, 0, 0)
    # g.add_edge(19, 0, 5, 9, 2)
    # g.add_edge(5, 5, 0, 1, 6)
    # g.add_edge(0, 9, 1, 0, 1)
    # g.add_edge(0, 2, 6, 1, 0)

    node = 0
    g.primMST(node)
