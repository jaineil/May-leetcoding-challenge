class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        z = num**0.5
        if z == int(z):
            return True
        else:
            return False