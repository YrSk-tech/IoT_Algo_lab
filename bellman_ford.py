N = 0
start_element = 0
graph = []


def read_data():
    with open('bellman_ford.in') as f:
        global N
        global start_element
        global graph
        for row in f:
            if (N == 0):
                data_str = row.split()
                N = int(data_str[0])  # number вершин
                start_element = int(data_str[1])
            else:
                data_str = row.split()
                u_v_w = [int(x) for x in data_str]
                graph.append(u_v_w)


def main():
    read_data()
    # ініціалізація максимальними знавченнями
    dist = [float("Inf")] * N
    dist[start_element] = 0
    # перебір всіх ребер для пошуку найкоротшого шляху
    for i in range(N - 1):
        for u, v, w in graph:
            if dist[u] != float("Inf") and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w

    for u, v, w in graph:
        if dist[u] != float("Inf") and dist[v] > dist[u] + w:
            print("Граф містить негативний цикл")

    sum = 0
    points = 0
    for i in range(0, N):
        if dist[i] != float("Inf"):
            sum += dist[i]
            points += 1
            print(i, dist[i])

    average = sum / (points - 1)

    with open("bellman_ford.out", "w") as f_out:
        f_out.write(str(average).format("{.:2f}"))
        f_out.close()


if __name__ == "__main__":
    main()