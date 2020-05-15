class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        
        def Kadane(nums):
            currSum, maxSum = nums[0], nums[0]
            for n in nums[1:]:
                currSum = max(n, currSum + n)
                maxSum = max(currSum, maxSum)
            return maxSum
        
        k = Kadane(A)
        cs = 0
        
        for i in range(len(A)):
            cs += A[i]
            A[i] = -A[i]
        
        cs += Kadane(A)
        
        if cs > k and cs != 0:
            return cs
        else:
            return k
        
    