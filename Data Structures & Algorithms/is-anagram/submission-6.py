class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # lengths differ then not a valid anagram
        if len(s) != len(t): 
            return False

        # frequency array
        count = [0] * 26
        
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1 # increment occurances map to array
            count[ord(t[i]) - ord('a')] -= 1 # decrement occurances map to array

        for val in count:
            if val != 0:
                return False
        return True

        