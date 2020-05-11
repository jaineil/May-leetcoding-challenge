class Solution:
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        
        def fill(image: List[List[int]], i: int, j: int, color: int, newColor: int):
        
        # pretty simple DFS 
        # we have 2 parts to the base case
        # we have to take care of boundary pixels by checking up,down,left,right
        # we have to check if the pixel we are at has the same color as (sr,sc) 
        
            if (i < 0 or i >= len(image)) or (j < 0 or j >= len(image[i])) or (image[i][j] != color):
                return
            image[i][j] =  newColor
            fill(image, i+1, j, color, newColor)
            fill(image, i-1, j, color, newColor)
            fill(image, i, j+1, color, newColor)
            fill(image, i, j-1, color, newColor)
        
        fill(image, sr, sc, image[sr][sc], newColor)
        return image
    
    