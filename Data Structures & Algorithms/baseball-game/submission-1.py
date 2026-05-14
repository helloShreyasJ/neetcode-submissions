class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        
        for o in operations:
            if o == 'C' or o == '+' or o == 'D':
                if o == 'C':
                    res -= stack.pop()
                elif o == '+':
                    res += int(stack[-1]) + int(stack[-2])
                    stack.append(int(stack[-1]) + int(stack[-2]))
                elif o == 'D':
                    res += (2 * stack[-1])
                    stack.append(int(stack[-1]) * 2)
            else:
                res += int(o)
                stack.append(int(o))
                
        return res