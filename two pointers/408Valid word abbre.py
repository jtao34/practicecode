class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isdigit():
                if abbr[j] == "0":
                    return False
                value = 0
                while j < len(abbr) and abbr[j].isdigit():
                    value = value * 10 + int(abbr[j])
                    j += 1
                i += value
            else:
                return False
        #corner case word = e, abbr = 2 
        return i == len(word) and j == len(abbr)