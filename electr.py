import math

class Electr:
    def __init__(self, distance, pillar_heights):
        self.__distance = distance
        self.__pillar_heights = pillar_heights
        self.__wire_length = 0

    def get_cable_length(self):
        calculated_hypotenuses = [[]]
        pillar_height = self.__pillar_heights
        amount_pillar_heights = len(self.__pillar_heights)

        for i in range(1, amount_pillar_heights):
            if i + 1 >= amount_pillar_heights:
                if pillar_height[i] > pillar_height[i - 1]:
                    pillar_height[i - 1] = 1
                    break
                if pillar_height[i] < pillar_height[i - 1]:
                    pillar_height[i] = 1
                    break
                break

            if pillar_height[i - 1] <= pillar_height[i] and pillar_height[i + 1] <= pillar_height[i]:
                pillar_height[i - 1] = 1
                pillar_height[i + 1] = 1
            elif pillar_height[i - 1] > pillar_height[i]:
                pillar_height[i] = 1
            elif pillar_height[i + 1] > pillar_height[i] and pillar_height[i - 1] != 1:
                pillar_height[i] = 1

        for i in range(1, amount_pillar_heights):
            self.calculate_cable(pillar_height[i - 1], pillar_height[i], calculated_hypotenuses)

        print(round(self.__wire_length, 2))
        return round(self.__wire_length, 2)



    def calculate_cable(self, start_pillar_height, end_pillar_height, calculated_hypotenuses):
        calculated_hypotenuse = max(calculated_hypotenuses, key=lambda x: x[2] if (
                start_pillar_height in x[:2] and end_pillar_height in x[:2]) else 0)
        if start_pillar_height == end_pillar_height:
            self.__wire_length += self.__distance
        elif calculated_hypotenuse:
            self.__wire_length += calculated_hypotenuse[2]
        else:
            a = end_pillar_height - start_pillar_height
            c = math.sqrt(math.pow(self.__distance, 2) + math.pow(a, 2))
            calculated_hypotenuses.append([start_pillar_height, end_pillar_height, c])
            self.__wire_length += c
        return self.__wire_length



if __name__ == '__main__':

    input_file = open("electr.in", "r")
    distance = int(input_file.readline())
    heights_line = input_file.readline()
    heights = [int(x) for x in heights_line.split()]

    g = Electr(distance, heights)

    output_file = open("electr.out", "w")
    output_file.write(str(g.get_cable_length()))

