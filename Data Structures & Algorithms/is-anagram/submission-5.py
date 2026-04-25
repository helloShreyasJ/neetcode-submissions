class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 2 dictionaries a, b that keep track of the characters in s, t
        a = {} # map char to occurance
        b = {} # map char to occurance

        for c in s:
            a[c] = a.get(c,0) + 1

        for c in t:
            b[c] = b.get(c,0) + 1

        return a == b

        