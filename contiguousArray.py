class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0: -1}
        net = 0
        maxx = 0

        for i, x in enumerate(nums):
            if x == 1:
                net += 1
            else:
                net -= 1

            if net in d: 
                l = i - d[net] 
                if l > maxx: 
                    maxx = l
            else:
                d[net] = i

        return maxx