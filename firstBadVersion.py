# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


''' The naive solution to this is iterating for all numbers from 1 to n.
However, it leads to O(n) complexity and TLE when value of n is too big. 
The better solution to this is using binary search and bringing the complexing down to O(log n) '''

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        while left < right:
            pivot = (left + right) // 2  
            quality = isBadVersion(pivot)
            if(quality==False):
                left = pivot+1            
            else:
                right = pivot
        return left