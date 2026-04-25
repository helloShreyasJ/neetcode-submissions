class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            sol[sortedS].append(s)
        return list(sol.values())


            