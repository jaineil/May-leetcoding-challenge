from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        string = list(s)
        counter = Counter(s)
        x = -99999
        for i in counter:
            if counter[i] == 1:
                x = i
                break
        
        if x == -99999:
            return -1
        else:
            return string.index(x)