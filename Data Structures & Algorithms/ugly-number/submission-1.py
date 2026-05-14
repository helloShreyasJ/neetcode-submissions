class Solution:
    def isUgly(self, n: int) -> bool:
        # edge case
        if n == 1:
            return True

        if n <= 0:
            return False

        # Keep track of the prime factors
        pf = []
        while n % 2 == 0:
            pf.append(2)
            n //= 2

        i = 3
        while i * i <= n:
            while n % i == 0:
                pf.append(i)
                n //= i
            i += 2
        
        if n > 2:
            pf.append(n)

        for factor in pf:
            if factor not in [2, 3, 5]:
                return False
        return True