class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = sorted(nums)
        # element that appears more than n/2 times has to be at midpoint
        return n[int(len(nums)/2)] 