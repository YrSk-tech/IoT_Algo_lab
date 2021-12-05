class Graph:
    def __init__(self, verticles):
        self.verticle = verticles
        self.graph = []

    def add_edge(self, a, b, c, d, e):
        self.graph.append([a, b, c, d, e])

    def print_solution(self, graph, first_parametr, secound_parametr):
        print(str(first_parametr) + "-" + str(secound_parametr) + ":" + str(graph[first_parametr][secound_parametr]))

    def algo(self, selected_node):
        INF = 9999999
        no_edge = 0
        selected_node[0] = True
        while no_edge < self.verticle - 1:

            minimum = INF
            a = 0
            b = 0
            for m in range(self.verticle):
                if selected_node[m]:
                    for n in range(self.verticle):
                        if (not selected_node[n]) and self.graph[m][n]:
                            if minimum > self.graph[m][n]:
                                minimum = self.graph[m][n]
                                a = m
                                b = n
            self.print_solution(self.graph, a, b)
            selected_node[b] = True
            no_edge += 1


if __name__ == '__main__':
    g = Graph(5)

    g.add_edge(0, 19, 5, 0, 0)
    g.add_edge(19, 0, 5, 9, 2)
    g.add_edge(5, 5, 0, 1, 6)
    g.add_edge(0, 9, 1, 0, 1)
    g.add_edge(0, 2, 6, 1, 0)

    selected_node = [0, 0, 0, 0, 0]
    print(g.algo(selected_node))
