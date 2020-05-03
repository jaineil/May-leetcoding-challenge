from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)
        c = 0
        for i in r:
            if i in m and r[i] <= m[i]:
                c += r[i]
        if c == len(ransomNote):
            return True
        else:
            return False