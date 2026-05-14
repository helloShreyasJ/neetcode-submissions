class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        idx = 0

        for c in s:
            dict[c] = dict.get(c, 0) + 1

        for c in s:
            if c in dict and dict[c] == 1:
                return idx
            idx += 1

        return -1