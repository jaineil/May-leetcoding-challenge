class Solution:
    # based on examples.. 
    # ..the question wants us to find permutations, not anagrams, that's the mistake 
    
    ''' 
    LOGIC..
    First, replacing all characters with their respective prime no.
    Hence, targetSum = sum of all characters in p.
    Computing the sum of each substring of len(p), going from left to right, 
    and if sum == targetSum, then we are appending corresponding starting index to result.
    Take primes whose adjacent difference is increasing from left to right, so that it gets different       sum for different anagrams.
    '''
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(s) == 0: return []
        
        primes = [2, 3, 5, 11, 19, 23, 37, 47, 59, 79, 97, 113, 137, 163, 191, 223, 257, 293, 331, 353, 383, 431, 487, 541, 587, 631]
        dictionary = {}
        result = []
        
        for c in "qwertyuiopasdfghjklzxcvbnm":
            dictionary[c] = primes[ord(c)-ord("a")]
        target = 0
        for i in p:
            target += dictionary[i]
        ln = len(p)
        
        check = 0
        l = 0
        for i in range(len(s)):
            check += dictionary[s[i]]
            l += 1
            if l==ln:
                if check == target: result.append(i-ln+1)
                check -= dictionary[s[i-ln+1]]
                l -= 1
            
        return result