class Kmp:

    def print_solution(self, solution):
        return print("Found pattern at index " + str(solution))

    def Search(self, pattern, txt):
        length_of_pattern = len(pattern)
        length_of_txt = len(txt)

        longest_prefix_suffix = [0] * length_of_pattern
        j = 0

        self.calculation_prefix_suffics(pattern, length_of_pattern, longest_prefix_suffix)

        i = 0
        while i < length_of_txt:
            if pattern[j] == txt[i]:
                i += 1
                j += 1

            if j == length_of_pattern:
                solution = i - j
                self.print_solution(solution)
                j = longest_prefix_suffix[j - 1]

            elif i < length_of_txt and pattern[j] != txt[i]:

                if j != 0:
                    j = longest_prefix_suffix[j - 1]
                else:
                    i += 1

    def calculation_prefix_suffics(self, pattern, length_of_pattern, longest_prefix_suffix):
        prefix_suffics = 0
        longest_prefix_suffix[0]
        i = 1

        while i < length_of_pattern:
            if pattern[i] == pattern[prefix_suffics]:
                prefix_suffics += 1
                longest_prefix_suffix[i] = prefix_suffics
                i += 1
            else:

                if prefix_suffics != 0:
                    prefix_suffics = longest_prefix_suffix[prefix_suffics - 1]

                else:
                    longest_prefix_suffix[i] = 0
                    i += 1


if __name__ == '__main__':
    txt = "ABABDABACDABABCABABCCASSDDDABABCABAB"
    pattern = "ABABCABAB"
    g = Kmp()
    g.Search(pattern, txt)
