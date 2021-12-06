import sys


class Graph:
    def __init__(self, verticles):
        self.verticle = verticles
        self.graph = []

    def add_edge(self, a, b, c, d, e):
        self.graph.append([a, b, c, d, e])

    def print_solution(self, parent):
        for i in range(1, self.verticle):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])


    def minKey(self, key, mstSet):

        min_value = sys.maxsize

        for v in range(self.verticle):
            if key[v] < min_value and mstSet[v] == False:
                min_value = key[v]
                min_index = v

        return min_index

    def primMST(self, node):

        key = [sys.maxsize] * self.verticle
        parent = [None] * self.verticle
        key[node] = 0
        mstSet = [False] * self.verticle

        parent[node] = -1

        for cout in range(self.verticle):

            u = self.minKey(key, mstSet)

            mstSet[u] = True

            for v in range(self.verticle):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_solution(parent)
        return mstSet


if __name__ == '__main__':
    g = Graph(5)

    g.add_edge(0, 19, 5, 0, 0)
    g.add_edge(19, 0, 5, 9, 2)
    g.add_edge(5, 5, 0, 1, 6)
    g.add_edge(0, 9, 1, 0, 1)
    g.add_edge(0, 2, 6, 1, 0)

    node = 0
    g.primMST(node)