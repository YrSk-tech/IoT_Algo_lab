class Kmp:
    def Search(self, pattern, txt):
        length_of_pattern = len(pattern)
        amount_of_txt = len(txt)

        # create lps[] that will hold the longest prefix suffix
        # values for pattern
        longest_prefix_suffix = [0] * length_of_pattern
        j = 0  # index for pat[]

        # Preprocess the pattern (calculate lps[] array)
        self.computeLPSArray(pattern , length_of_pattern, longest_prefix_suffix)

        i = 0  # index for txt[]
        while i < amount_of_txt:
            if pattern[j] == txt[i]:
                i += 1
                j += 1

            if j == length_of_pattern:
                print("Found pattern at index " + str(i - j))
                j = longest_prefix_suffix[j - 1]

            # mismatch after j matches
            elif i < amount_of_txt and pattern [j] != txt[i]:
                # Do not match lps[0..lps[j-1]] characters,
                # they will match anyway
                if j != 0:
                    j = longest_prefix_suffix[j - 1]
                else:
                    i += 1

    def computeLPSArray(self,pattern ,  M, lps):

        lps[0]  # lps[0] is always 0
        i = 1

        while i < M:
            if pattern[i] == pattern[temporary_length_pattern]:
                temporary_length_pattern += 1
                lps[i] = temporary_length_pattern
                i += 1
            else:

                if temporary_length_pattern != 0:
                    temporary_length_pattern = lps[temporary_length_pattern - 1]

                else:
                    lps[i] = 0
                    i += 1


if __name__ == '__main__':

    txt = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    g = Kmp()
    g.Search(pattern, txt)