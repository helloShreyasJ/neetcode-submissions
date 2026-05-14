class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        
        for o in operations:
            if o == 'C' or o == '+' or o == 'D':
                if o == 'C':
                    stack.pop()
                elif o == '+':
                    stack.append(int(stack[-1]) + int(stack[-2]))
                elif o == 'D':
                    stack.append(int(stack[-1]) * 2)
            else:
                stack.append(int(o))
                
            res = sum(stack)
        return res