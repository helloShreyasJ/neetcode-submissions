class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        def merge(str1, str2):
            result = []
            i = j = 0
            while i < len(str1) and j < len(str2):
                result.append(str1[i])
                i += 1
                result.append(str2[j])
                j += 1
            result.extend(str1[i:])
            result.extend(str2[j:])
            return "".join(result)
        return merge(word1, word2)
