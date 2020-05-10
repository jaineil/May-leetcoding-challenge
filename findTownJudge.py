class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trusters = {t[0] for t in trust}
        trustedBy = 0
        judge = -1
        for i in range(1, N+1):
            if i not in trusters:
                judge = i
        
        for a, b in trust:
            if b == judge:
                trustedBy += 1
        
        if trustedBy != N - 1:
            judge = -1
            
        return judge