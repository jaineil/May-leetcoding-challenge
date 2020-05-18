class Solution:
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1Len, s2Len = len(s1), len(s2)
        s1Hash, s2Hash = 0, 0
        if s1Len > s2Len:
            return False
        
        for i in range(s1Len):
            s1Hash, s2Hash = s1Hash + hash(s1[i]), s2Hash + hash(s2[i])
            
        if s1Hash == s2Hash:
            return True
        
        for i in range(s1Len, s2Len):
            s2Hash += hash(s2[i]) - hash(s2[i-s1Len])
            if s2Hash == s1Hash:
                return True
            
        return False