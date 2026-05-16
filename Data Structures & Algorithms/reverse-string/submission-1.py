class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        stack = []
        for c in s:
            stack.append(c)
        
        for i in range(len(stack)):
            s[i] = stack.pop()
