from math import sqrt


class Algo:
    def __init__(self):
        self.heist = []
        self.c = 0
    def input_data(self, n):
        self.heist.append(n)

    def print_solution(self, c):
        return print(c)

    def electr(self, distance):
        amount_of_heist = len(self.heist)
        if amount_of_heist != 0:
            for i in range(amount_of_heist- 1):
                if self.heist[i] < self.heist[i + 1]:
                    a = self.heist[i + 1] - self.heist[i]
                else:
                    a = self.heist[i] - self.heist[i + 1]
                b = distance
                if a == self.heist[i+1]:
                    self.c += distance
                self.c += sqrt(int(b)**2 + int(a)**2)
        self.print_solution(self.c)


if __name__ == '__main__':
    w = int(input("enter distance between support"))
    g = Algo()
    g.input_data(3)
    g.input_data(1)
    g.input_data(3)
    g.electr(w)
